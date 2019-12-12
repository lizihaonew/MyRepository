# -*- coding: utf-8 -*-
import random
import pytest
from UI.base_case import BaseUITestCase, SmokeTestMixin
from ..pages.asset_configuration_page import AssetConfigurationPage


class AssetConfigurationTestCase(BaseUITestCase):

    def setUp(self):
        self.asset_configuration_page = AssetConfigurationPage(self.browser)

    def test_new_asset_configuration(self):
        asset_name = self.asset_configuration_page.new_asset_configuration(risk_type_index=random.randint(0, 4),
                                                                           category_number=random.randint(1, 5),
                                                                           product_number=random.randint(1, 4))
        query_asset_name = self.asset_configuration_page.query_asset_configuration(asset_name)['asset_name'][0]
        self.assertEqual(asset_name, query_asset_name)

    def test_delete_asset_configuration(self):
        self.asset_configuration_page.delete_asset_configuration(-1)

    def test_modify_asset_configuration(self):
        picked_asset_name = self.asset_configuration_page.get_asset_configuration_names()
        changed_asset_name = self.asset_configuration_page.modify_asset_configuration(picked_asset_name)
        query_asset_name = self.asset_configuration_page.query_asset_configuration(changed_asset_name)['asset_name'][0]
        self.assertEqual(changed_asset_name, query_asset_name)
        self.asset_configuration_page.modify_asset_configuration(query_asset_name, picked_asset_name)


@pytest.mark.smoke
class AssetConfigurationSmokeTest(SmokeTestMixin, BaseUITestCase):
    """
    Smoke test for asset configuration
    """
    page_class = AssetConfigurationPage