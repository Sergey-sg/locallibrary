from django.test import TestCase
from ..models import Author, Book, BookInstance, Genre, Language


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(), '/catalog/author/1')


class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        author = Author(first_name="Mazuki", last_name="Sekida", date_of_birth='1988-10-20')
        author.save()
        genre = Genre(name='ggg')
        genre.save()
        language = Language(name='Ukrainian')
        language.save()
        # Set up non-modified objects used by all test methods
        Book.objects.create(title='test title', author=author, summary='test summary', isbn='4444444444444', language=language)

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_last_name_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_summary_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('summary').verbose_name
        self.assertEquals(field_label, 'summary')

    def test_isbn_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEquals(field_label, 'ISBN')

    def test_genre_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('genre').verbose_name
        self.assertEquals(field_label, 'genre')

    def test_language_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('language').verbose_name
        self.assertEquals(field_label, 'language')

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_summary_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('summary').max_length
        self.assertEquals(max_length, 1000)

    def test_isbn_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('isbn').max_length
        self.assertEquals(max_length, 13)

    def test_author_is_author(self):
        book = Book.objects.get(id=1)
        field_author = book.author
        self.assertTrue(type(field_author) is Author)

    # def test_genre_is_genre(self):
    #     book = Book.objects.get(id=1)
    #     field_genre = book.genre
    #     self.assertEquals(type(field_genre), Genre)

    def test_language_is_language(self):
        book = Book.objects.get(id=1)
        field_language = book.language
        self.assertEquals(type(field_language), Language)

    def test_object_name_is_title(self):
        book = Book.objects.get(id=1)
        expected_object_name = book.title
        self.assertEquals(expected_object_name, str(book))

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(book.get_absolute_url(), '/catalog/book/1')


class GenreModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Genre.objects.create(name='ggg')

    def test_name_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_object_name_is_name(self):
        genre = Genre.objects.get(id=1)
        expected_object_name = genre.name
        self.assertEquals(expected_object_name, str(genre))


class LanguageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Language.objects.create(name='Ukrainian')

    def test_name_label(self):
        language = Language.objects.get(id=1)
        field_label = language._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        language = Language.objects.get(id=1)
        max_length = language._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_object_name_is_name(self):
        language = Language.objects.get(id=1)
        expected_object_name = language.name
        self.assertEquals(expected_object_name, str(language))


class BookInstanceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        author = Author(first_name="Mazuki", last_name="Sekida", date_of_birth='1988-10-20')
        author.save()
        genre = Genre(name='ggg')
        genre.save()
        language = Language(name='Ukrainian')
        language.save()
        book = Book(title='test title', author=author, summary='test summary', isbn='4444444444444', language=language)
        book.save()
        # Set up non-modified objects used by all test methods
        BookInstance.objects.create(id='fd07e07b-0328-4f9c-bc2e-f7f6a1d815b6', book=book, imprint='paper')

    def test_book_label(self):
        bookinstance = BookInstance.objects.get(id='fd07e07b-0328-4f9c-bc2e-f7f6a1d815b6')
        field_label = bookinstance._meta.get_field('book').verbose_name
        self.assertEquals(field_label, 'book')

    def test_book_is_Book(self):
        bookinstance = BookInstance.objects.get(id='fd07e07b-0328-4f9c-bc2e-f7f6a1d815b6')
        field_book = bookinstance.book
        self.assertEquals(type(field_book), Book)

    def test_imprint_label(self):
        bookinstance = BookInstance.objects.get(id='fd07e07b-0328-4f9c-bc2e-f7f6a1d815b6')
        field_label = bookinstance._meta.get_field('imprint').verbose_name
        self.assertEquals(field_label, 'imprint')

    def test_imprint_max_length(self):
        bookinstance = BookInstance.objects.get(id='fd07e07b-0328-4f9c-bc2e-f7f6a1d815b6')
        max_length = bookinstance._meta.get_field('imprint').max_length
        self.assertEquals(max_length, 200)
