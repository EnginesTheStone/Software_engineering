from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import myCards, Cart
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.


class myCardsTestCase(TestCase):
    def setUp(self):
        #sample card creation#
        self.card = myCards.objects.create(
            cardname="test card",
            cardprice=15,
            stock=3
    )
        
    def test_card_made(self):
        #test for saved card#
        card = myCards.objects.get(cardname="test card")
        self.assertEqual(card.cardprice, 15)
        self.assertEqual(card.stock, 3)

    def test_card_str_method(self):
        #check str method work#
        self.assertEqual(str(self.card), "test card")

class cartTestcase(TestCase):
    def setUp(self):
        #creat card and user#
        self.User = User.objects.create_user(username="testuser", password="Password123!")
        self.card = myCards.objects.create(cardname="test card", cardprice=12, stock=5)
        self.cart_item = Cart.objects.create(user=self.User, product=self.card, quantity=2)

    def test_cart_create(self):
        #check if item is saved in cart#
        self.assertEqual(self.cart_item.user.username, "testuser")
        self.assertEqual(self.cart_item.product.cardname, "test card")
        self.assertEqual(self.cart_item.quantity, 2)

    def test_cart_price(self):

        self.assertEqual(self.cart_item.get_total_price(), 24)

    def test_cart_str(self):
        self.assertEqual(str(self.cart_item), "test card (x2)")

class viewsTestCase(TestCase):
    def setUp(self):
        #make test user and product#
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="Password123!")
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpg")
        self.card = myCards.objects.create(cardname="test card", cardprice=13, stock=3, cardimage=image)


    def testHomePage(self):
        #check home page loads#
        response = self.client.get('/cards/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def testBuyPage(self):
        #check products are displayed and page loads#
        response = self.client.get('/cards/buy/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test card")

    def testCheckoutNonAccount(self):
        #check for redirect when not logged in#
        response = self.client.get('/cards/checkout/')
        self.assertNotEqual(response.status_code, 200)

        #now logged in#
        self.client.login(username="testuser", password="Password123!")
        response = self.client.get('/cards/checkout/')
        self.assertEqual(response.status_code, 200)

    def testAddtoCart(self):
        #chcecking items get add to the cart#
        self.client.login(username="testuser", password="Password123!")
        response = self.client.get(f'/cards/add_to_cart/{self.card.id}/')
        self.assertEqual(response.status_code, 302)

        cart_item = Cart.objects.get(user=self.user, product=self.card)
        self.assertEqual(cart_item.quantity, 1)

    def testViewCart(self):
        #checking cart#
        self.client.login(username="testuser", password="Password123!")
        Cart.objects.create(user=self.user, product=self.card, quantity=2)
        response = self.client.get('/cards/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test card")

    def removeFromCart(self):
        #removing items from cart#
        self.client.login(username="testuser", password="Password123!")
        cart_item = Cart.objects.create(user=self.user, product=self.card, quantity=1)
        response = self.client.get(f'/cards/remove_from_cart/{cart_item.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Cart.objects.filter(id=cart_item.id).exists())

    def testPurchaseComplete(self):
        #checking if loads up correctly#
        self.client.login(username="testuser", password="Password123!")
        Cart.objects.create(user=self.user, product=self.card, quantity=2)
        response = self.client.get('/cards/purchase_confirmation/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Cart.objects.filter(user=self.user).exists())