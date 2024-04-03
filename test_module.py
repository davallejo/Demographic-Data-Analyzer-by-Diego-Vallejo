#test_module.py
#Autor: Diego Armando Vallejo Vinueza

import unittest
import demographic_data_analyzer

class DemographicAnalyzerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = demographic_data_analyzer.calculate_demographic_data(print_data=False)

    def test_race_count(self):
        actual = self.data['race_count'].tolist()
        expected = [27816, 3124, 1039, 311, 271]
        self.assertCountEqual(actual, expected, msg="Expected race count values to be [27816, 3124, 1039, 311, 271]")

    def test_average_age_men(self):
        expected = 39.4
        actual = round(self.data['average_age_men'], 1)
        self.assertAlmostEqual(actual, expected, msg="Expected different value for average age of men.")

    def test_percentage_bachelors(self):
        expected = 16.4 
        actual = round(self.data['percentage_bachelors'], 1)
        self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage with Bachelors degrees.")

    def test_higher_education_rich(self):
        expected = 46.5
        actual = round(self.data['higher_education_rich'], 1)
        self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage with higher education that earn >50K.")

    def test_lower_education_rich(self):
        expected = 17.4
        actual = round(self.data['lower_education_rich'], 1)
        self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage without higher education that earn >50K.")

    def test_min_work_hours(self):
        expected = 1
        actual = self.data['min_work_hours']
        self.assertAlmostEqual(actual, expected, msg="Expected different value for minimum work hours.")     

    def test_rich_percentage(self):
        expected = 10
        actual = round(self.data['rich_percentage'], 1)
        self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage of rich among those who work fewest hours.")   

    def test_highest_earning_country(self):
        expected = 'United-States'
        actual = self.data['highest_earning_country']
        self.assertEqual(actual, expected, "Expected different value for highest earning country.")   

    def test_highest_earning_country_percentage(self):
        expected = 24.6
        actual = round(self.data['highest_earning_country_percentage'], 1)
        self.assertAlmostEqual(actual, expected, places=1, msg="Expected different value for highest earning country percentage.")   

    def test_top_IN_occupation(self):
        expected = 'Prof-specialty'
        actual = self.data['top_IN_occupation']
        self.assertEqual(actual, expected, "Expected different value for top occupations in India.")      

if __name__ == "__main__":
    unittest.main()
