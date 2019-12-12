from UI.base_element import ElementCollection, AsyncElement
from UI.special_elements.select2_element import Select2Element
from UI.special_elements.select_element import SelectElement


class AddAssetConfigurationElementCollection(ElementCollection):

    smoke_locators = []

    def __init__(self):
        self.asset_name = AsyncElement('#name')
        self.asset_introduction = AsyncElement('#introduction')
        self.asset_risk_type = AsyncElement('[class^="riskTolerance"]')
        self.add_part = AsyncElement('#add_part')
        self.asset_category = Select2Element('#add_category .select2')
        self.ratio = AsyncElement('.ratio')
        self.choose_product = AsyncElement('.add_asset_product')
        self.product_category = SelectElement('select[name="category"]')
        self.product_checkbox = AsyncElement('.checkbox_position')
        self.query_product = AsyncElement('.query_productList')
        self.confirm_product_selection = AsyncElement('.js-ok')
        self.submit_add_button = AsyncElement('#_submit')


class AssetConfigurationListElementCollection(ElementCollection):

    smoke_locators = ['add_asset', 'asset_allocation_name', 'query_asset']

    def __init__(self):
        self.add_asset = AsyncElement('#_add')
        self.asset_allocation_name = AsyncElement('#assetAllocationName')
        self.query_asset = AsyncElement('#_query')
        self.query_asset_name = AsyncElement('.gradeX ._details')
        self.modify = AsyncElement('.update')
        self.delete = AsyncElement('._delete')
        self.confirm_delete = AsyncElement('.js-ok')
        self.action_tip = AsyncElement('.content.js-tip')
