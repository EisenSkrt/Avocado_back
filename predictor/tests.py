import pytest
from django.test import TestCase
from .models import PredictionInput

API_PATH = '/predictorInput/?format=api'

class PredictionInputTests(TestCase):
    fixtures = ["predictionInput.json"]

    def test_valid_input(self):
        '''
        Test that a valid input will be entered through the API successfully
        '''
        valid_input = PredictionInput.objects.get(pk=1).__dict__
        response = self.client.post(path=API_PATH, data=valid_input)
        self.assertEqual(response.status_code, 201)

    def test_non_float_total_volume(self):
        '''
        Test that a non float value for the total volume input will not be entered through the API successfully
        '''
        string_input = PredictionInput.objects.get(pk=1).__dict__
        string_input['total_volume'] = "test"
        response = self.client.post(path=API_PATH, data=string_input)
        self.assertContains(
            response=response,
            text="A valid number is required",
            status_code=400,
            )

    def test_negative_total_volume(self):
        '''
        Test that a negative value for the total volume input will not be entered through the API successfully
        '''
        negative_input = PredictionInput.objects.get(pk=1).__dict__
        negative_input['total_volume'] = -1
        response = self.client.post(path=API_PATH, data=negative_input)
        self.assertContains(
            response=response,
            text="Ensure this value is greater than or equal to 0.0",
            status_code=400,
        )

    def test_zero_total_volume(self):
        '''
        Test that a zero value for the total volume input will be entered through the API successfully
        '''
        zero_input = PredictionInput.objects.get(pk=1).__dict__
        zero_input['total_volume'] = 0
        response = self.client.post(path=API_PATH, data=zero_input)
        self.assertEqual(response.status_code, 201)

    def test_non_float_small_avocado(self):
        '''
        Test that a non float value for the small avocado input will not be entered through the API successfully
        '''
        string_input = PredictionInput.objects.get(pk=1).__dict__
        string_input['small_avo'] = "test"
        response = self.client.post(path=API_PATH, data=string_input)
        self.assertContains(
            response=response,
            text="A valid number is required",
            status_code=400,
        )

    def test_negative_small_avocado(self):
        '''
        Test that a negative value for the small avocado input will not be entered through the API successfully
        '''
        negative_input = PredictionInput.objects.get(pk=1).__dict__
        negative_input['small_avo'] = -1
        response = self.client.post(path=API_PATH, data=negative_input)
        self.assertContains(
            response=response,
            text="Ensure this value is greater than or equal to 0.0",
            status_code=400,
        )

    def test_zero_small_avocado(self):
        '''
        Test that a zero value for the small avocado input will be entered through the API successfully
        '''
        zero_input = PredictionInput.objects.get(pk=1).__dict__
        zero_input['small_avocado'] = 0
        response = self.client.post(path=API_PATH, data=zero_input)
        self.assertEqual(response.status_code, 201)

    def test_non_float_large_avocado(self):
        '''
        Test that a non float value for the large avocado input will not be entered through the API successfully
        '''
        string_input = PredictionInput.objects.get(pk=1).__dict__
        string_input['large_avo'] = "test"
        response = self.client.post(path=API_PATH, data=string_input)
        self.assertContains(
            response=response,
            text="A valid number is required",
            status_code=400,
        )

    def test_negative_large_avocado(self):
        '''
        Test that a negative value for the large avocado input will not be entered through the API successfully
        '''
        negative_input = PredictionInput.objects.get(pk=1).__dict__
        negative_input['large_avo'] = -1
        response = self.client.post(path=API_PATH, data=negative_input)
        self.assertContains(
            response=response,
            text="Ensure this value is greater than or equal to 0.0",
            status_code=400,
        )

    def test_zero_large_avocado(self):
        '''
        Test that a zero value for the large avocado input will be entered through the API successfully
        '''
        zero_input = PredictionInput.objects.get(pk=1).__dict__
        zero_input['large_avocado'] = 0
        response = self.client.post(path=API_PATH, data=zero_input)
        self.assertEqual(response.status_code, 201)

    def test_non_float_xl_avocado(self):
        '''
        Test that a non float value for the xl avocado input will not be entered through the API successfully
        '''
        string_input = PredictionInput.objects.get(pk=1).__dict__
        string_input['xl_avo'] = "test"
        response = self.client.post(path=API_PATH, data=string_input)
        self.assertContains(
            response=response,
            text="A valid number is required",
            status_code=400,
        )

    def test_negative_xl_avocado(self):
        '''
        Test that a negative value for the xl avocado input will not be entered through the API successfully
        '''
        negative_input = PredictionInput.objects.get(pk=1).__dict__
        negative_input['xl_avo'] = -1
        response = self.client.post(path=API_PATH, data=negative_input)
        self.assertContains(
            response=response,
            text="Ensure this value is greater than or equal to 0.0",
            status_code=400,
        )

    def test_zero_xl_avocado(self):
        '''
        Test that a zero value for the xl avocado input will be entered through the API successfully
        '''
        zero_input = PredictionInput.objects.get(pk=1).__dict__
        zero_input['xl_avocado'] = 0
        response = self.client.post(path=API_PATH, data=zero_input)
        self.assertEqual(response.status_code, 201)

    def test_non_float_total_bags(self):
        '''
        Test that a non float value for the total bags input will not be entered through the API successfully
        '''
        string_input = PredictionInput.objects.get(pk=1).__dict__
        string_input['total_bags'] = "test"
        response = self.client.post(path=API_PATH, data=string_input)
        self.assertContains(
            response=response,
            text="A valid number is required",
            status_code=400,
        )

    def test_negative_total_bags(self):
        '''
        Test that a negative value for the total bags input will not be entered through the API successfully
        '''
        negative_input = PredictionInput.objects.get(pk=1).__dict__
        negative_input['total_bags'] = -1
        response = self.client.post(path=API_PATH, data=negative_input)
        self.assertContains(
            response=response,
            text="Ensure this value is greater than or equal to 0.0",
            status_code=400,
        )

    def test_zero_total_bags(self):
        '''
        Test that a zero value for the total bags input will be entered through the API successfully
        '''
        zero_input = PredictionInput.objects.get(pk=1).__dict__
        zero_input['total_bags'] = 0
        response = self.client.post(path=API_PATH, data=zero_input)
        self.assertEqual(response.status_code, 201)

    def test_non_float_small_bags(self):
        '''
        Test that a non float value for the small bags input will not be entered through the API successfully
        '''
        string_input = PredictionInput.objects.get(pk=1).__dict__
        string_input['small_bags'] = "test"
        response = self.client.post(path=API_PATH, data=string_input)
        self.assertContains(
            response=response,
            text="A valid number is required",
            status_code=400,
        )

    def test_negative_small_bags(self):
        '''
        Test that a negative value for the small bags input will not be entered through the API successfully
        '''
        negative_input = PredictionInput.objects.get(pk=1).__dict__
        negative_input['small_bags'] = -1
        response = self.client.post(path=API_PATH, data=negative_input)
        self.assertContains(
            response=response,
            text="Ensure this value is greater than or equal to 0.0",
            status_code=400,
        )

    def test_zero_small_bags(self):
        '''
        Test that a zero value for the small bags input will be entered through the API successfully
        '''
        zero_input = PredictionInput.objects.get(pk=1).__dict__
        zero_input['small_bags'] = 0
        response = self.client.post(path=API_PATH, data=zero_input)
        self.assertEqual(response.status_code, 201)

    def test_non_float_large_bags(self):
        '''
        Test that a non float value for the large bags input will not be entered through the API successfully
        '''
        string_input = PredictionInput.objects.get(pk=1).__dict__
        string_input['large_bags'] = "test"
        response = self.client.post(path=API_PATH, data=string_input)
        self.assertContains(
            response=response,
            text="A valid number is required",
            status_code=400,
        )

    def test_negative_large_bags(self):
        '''
        Test that a negative value for the large bags input will not be entered through the API successfully
        '''
        negative_input = PredictionInput.objects.get(pk=1).__dict__
        negative_input['large_bags'] = -1
        response = self.client.post(path=API_PATH, data=negative_input)
        self.assertContains(
            response=response,
            text="Ensure this value is greater than or equal to 0.0",
            status_code=400,
        )

    def test_zero_large_bags(self):
        '''
        Test that a zero value for the large bags input will be entered through the API successfully
        '''
        zero_input = PredictionInput.objects.get(pk=1).__dict__
        zero_input['large_bags'] = 0
        response = self.client.post(path=API_PATH, data=zero_input)
        self.assertEqual(response.status_code, 201)

    def test_non_float_xl_bags(self):
        '''
        Test that a non float value for the xl bags input will not be entered through the API successfully
        '''
        string_input = PredictionInput.objects.get(pk=1).__dict__
        string_input['xl_bags'] = "test"
        response = self.client.post(path=API_PATH, data=string_input)
        self.assertContains(
            response=response,
            text="A valid number is required",
            status_code=400,
        )

    def test_negative_xl_bags(self):
        '''
        Test that a negative value for the xl bags input will not be entered through the API successfully
        '''
        negative_input = PredictionInput.objects.get(pk=1).__dict__
        negative_input['xl_bags'] = -1
        response = self.client.post(path=API_PATH, data=negative_input)
        self.assertContains(
            response=response,
            text="Ensure this value is greater than or equal to 0.0",
            status_code=400,
        )

    def test_zero_xl_bags(self):
        '''
        Test that a zero value for the xl bags input will be entered through the API successfully
        '''
        zero_input = PredictionInput.objects.get(pk=1).__dict__
        zero_input['xl_bags'] = 0
        response = self.client.post(path=API_PATH, data=zero_input)
        self.assertEqual(response.status_code, 201)

    def test_invalid_choice_type(self):
        '''
        Test that an invalid choice for the type input will not be entered through the API successfully
        '''
        invalid_choice_input = PredictionInput.objects.get(pk=1).__dict__

        invalid_choice_input['type'] = "test"
        response = self.client.post(path=API_PATH, data=invalid_choice_input)
        self.assertContains(
            response=response,
            text="is not a valid choice",
            status_code=400,
        )

        invalid_choice_input['type'] = -1
        response = self.client.post(path=API_PATH, data=invalid_choice_input)
        self.assertContains(
            response=response,
            text="is not a valid choice",
            status_code=400,
        )

        invalid_choice_input['type'] = "test"
        response = self.client.post(path=API_PATH, data=invalid_choice_input)
        self.assertContains(
            response=response,
            text="is not a valid choice",
            status_code=400,
        )

    def test_all_choices_type(self):
        """
        Test that all of the available choices will be entered properly through the API
        """
        choice_input = PredictionInput.objects.get(pk=1).__dict__
        for choice in PredictionInput.AVOCADO_TYPES:
            choice_input['type'] = choice[0]
            response = self.client.post(path=API_PATH, data=choice_input)
            self.assertEqual(response.status_code, 201)

    def test_non_int_year(self):
        '''
        Test that a non integer value for the year input will not be entered through the API successfully
        '''
        invalid_year = PredictionInput.objects.get(pk=1).__dict__
        invalid_year['year'] = "test"
        response = self.client.post(path=API_PATH, data=invalid_year)
        self.assertContains(
            response=response,
            text="A valid integer is required",
            status_code=400,
        )

        invalid_year['year'] = 1.5
        response = self.client.post(path=API_PATH, data=invalid_year)
        self.assertContains(
            response=response,
            text="A valid integer is required",
            status_code=400,
        )
        self.assertContains(
            response=response,
            text="year",
            status_code=400,
        )

    def test_negative_year(self):
        '''
        Test that a negative value for the year input will not be entered through the API successfully
        '''
        negative_input = PredictionInput.objects.get(pk=1).__dict__
        negative_input['year'] = -1
        response = self.client.post(path=API_PATH, data=negative_input)
        self.assertContains(
            response=response,
            text="Ensure this value is greater than or equal to 0",
            status_code=400,
        )

    def test_zero_year(self):
        '''
        Test that a zero value for the year input will be entered through the API successfully
        '''
        zero_input = PredictionInput.objects.get(pk=1).__dict__
        zero_input['year'] = 0
        response = self.client.post(path=API_PATH, data=zero_input)
        self.assertEqual(response.status_code, 201)

    def test_long_region(self):
        '''
        Test that a long str value for the region input will not be entered through the API successfully
        '''
        long_string_input = PredictionInput.objects.get(pk=1).__dict__
        long_string_input['region'] = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1" # 51 Chars
        response = self.client.post(path=API_PATH, data=long_string_input)
        self.assertContains(
            response=response,
            text="Ensure this field has no more than 50 characters",
            status_code=400,
        )

    def test_non_str_region(self):
        '''
        Test that a non str value for the region input will be entered through the API successfully
        Every object can be converted to str
        '''
        int_input = PredictionInput.objects.get(pk=1).__dict__
        int_input['region'] = -1
        response = self.client.post(path=API_PATH, data=int_input)
        self.assertEqual(response.status_code, 201)
