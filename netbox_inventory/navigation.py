from netbox.plugins import (
    PluginMenu,
    PluginMenuButton,
    PluginMenuItem,
    get_plugin_config,
)

#
# Assets (Активы)
#

inventoryitemgroup_buttons = [
    PluginMenuButton(
        link='plugins:netbox_inventory:inventoryitemgroup_add',
        title='Добавить',
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_inventory.add_inventoryitemgroup'],
    ),
    PluginMenuButton(
        link='plugins:netbox_inventory:inventoryitemgroup_bulk_import',
        title='Импорт',
        icon_class='mdi mdi-upload',
        permissions=['netbox_inventory.add_inventoryitemgroup'],
    ),
]

inventoryitemtype_buttons = [
    PluginMenuButton(
        link='plugins:netbox_inventory:inventoryitemtype_add',
        title='Добавить',
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_inventory.add_inventoryitemtype'],
    ),
    PluginMenuButton(
        link='plugins:netbox_inventory:inventoryitemtype_bulk_import',
        title='Импорт',
        icon_class='mdi mdi-upload',
        permissions=['netbox_inventory.add_inventoryitemtype'],
    ),
]

asset_buttons = [
    PluginMenuButton(
        link='plugins:netbox_inventory:asset_add',
        title='Добавить',
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_inventory.add_asset'],
    ),
    PluginMenuButton(
        link='plugins:netbox_inventory:asset_bulk_import',
        title='Импорт',
        icon_class='mdi mdi-upload',
        permissions=['netbox_inventory.add_asset'],
    ),
]

assetrole_buttons = [
    PluginMenuButton(
        link='plugins:netbox_inventory:assetrole_add',
        title='Добавить',
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_inventory.add_assetrole'],
    ),
    PluginMenuButton(
        link='plugins:netbox_inventory:assetrole_bulk_import',
        title='Импорт',
        icon_class='mdi mdi-upload',
        permissions=['netbox_inventory.add_assetrole'],
    ),
]

assets_items = (
    PluginMenuItem(
        link='plugins:netbox_inventory:asset_list',
        link_text='Активы',
        permissions=['netbox_inventory.view_asset'],
        buttons=asset_buttons,
    ),
    PluginMenuItem(
        link='plugins:netbox_inventory:assetrole_list',
        link_text='Роли активов',
        permissions=['netbox_inventory.view_assetrole'],
        buttons=assetrole_buttons,
    ),
    PluginMenuItem(
        link='plugins:netbox_inventory:inventoryitemtype_list',
        link_text='Типы компонентов',
        permissions=['netbox_inventory.view_inventoryitemtype'],
        buttons=inventoryitemtype_buttons,
    ),
    PluginMenuItem(
        link='plugins:netbox_inventory:inventoryitemgroup_list',
        link_text='Группы компонентов',
        permissions=['netbox_inventory.view_inventoryitemgroup'],
        buttons=inventoryitemgroup_buttons,
    ),
)


#
# Deliveries (Поставки)
#

supplier_buttons = [
    PluginMenuButton(
        link='plugins:netbox_inventory:supplier_add',
        title='Добавить',
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_inventory.add_supplier'],
    ),
    PluginMenuButton(
        link='plugins:netbox_inventory:supplier_bulk_import',
        title='Импорт',
        icon_class='mdi mdi-upload',
        permissions=['netbox_inventory.add_supplier'],
    ),
]

purchase_buttons = [
    PluginMenuButton(
        link='plugins:netbox_inventory:purchase_add',
        title='Добавить',
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_inventory.add_purchase'],
    ),
    PluginMenuButton(
        link='plugins:netbox_inventory:purchase_bulk_import',
        title='Импорт',
        icon_class='mdi mdi-upload',
        permissions=['netbox_inventory.add_purchase'],
    ),
]

delivery_buttons = [
    PluginMenuButton(
        link='plugins:netbox_inventory:delivery_add',
        title='Добавить',
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_inventory.add_delivery'],
    ),
    PluginMenuButton(
        link='plugins:netbox_inventory:delivery_bulk_import',
        title='Импорт',
        icon_class='mdi mdi-upload',
        permissions=['netbox_inventory.add_delivery'],
    ),
]

deliveries_items = (
    PluginMenuItem(
        link='plugins:netbox_inventory:supplier_list',
        link_text='Поставщики',
        permissions=['netbox_inventory.view_supplier'],
        buttons=supplier_buttons,
    ),
    PluginMenuItem(
        link='plugins:netbox_inventory:purchase_list',
        link_text='Закупки',
        permissions=['netbox_inventory.view_purchase'],
        buttons=purchase_buttons,
    ),
    PluginMenuItem(
        link='plugins:netbox_inventory:delivery_list',
        link_text='Поставки',
        permissions=['netbox_inventory.view_delivery'],
        buttons=delivery_buttons,
    ),
)


#
# Audit (Аудит)
#

audit_admin_items = (
    PluginMenuItem(
        link='plugins:netbox_inventory:auditflow_list',
        link_text='Процессы аудита',
        permissions=['netbox_inventory.view_auditflow'],
        buttons=[
            PluginMenuButton(
                link='plugins:netbox_inventory:auditflow_add',
                title='Добавить',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_inventory.add_auditflow'],
            ),
            PluginMenuButton(
                link='plugins:netbox_inventory:auditflow_bulk_import',
                title='Импорт',
                icon_class='mdi mdi-upload',
                permissions=['netbox_inventory.add_auditflow'],
            ),
        ],
    ),
    PluginMenuItem(
        link='plugins:netbox_inventory:auditflowpage_list',
        link_text='Страницы процессов',
        permissions=['netbox_inventory.view_auditflowpage'],
        buttons=[
            PluginMenuButton(
                link='plugins:netbox_inventory:auditflowpage_add',
                title='Добавить',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_inventory.add_auditflowpage'],
            ),
            PluginMenuButton(
                link='plugins:netbox_inventory:auditflowpage_bulk_import',
                title='Импорт',
                icon_class='mdi mdi-upload',
                permissions=['netbox_inventory.add_auditflowpage'],
            ),
        ],
    ),
    PluginMenuItem(
        link='plugins:netbox_inventory:audittrail_list',
        link_text='Журнал аудита',
        permissions=['netbox_inventory.view_audittrail'],
        buttons=[
            PluginMenuButton(
                link='plugins:netbox_inventory:audittrail_bulk_import',
                title='Импорт',
                icon_class='mdi mdi-upload',
                permissions=['netbox_inventory.add_audittrail'],
            ),
        ],
    ),
    PluginMenuItem(
        link='plugins:netbox_inventory:audittrailsource_list',
        link_text='Источники аудита',
        permissions=['netbox_inventory.view_audittrailsource'],
        buttons=[
            PluginMenuButton(
                link='plugins:netbox_inventory:audittrailsource_add',
                title='Добавить',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_inventory.add_audittrailsource'],
            ),
            PluginMenuButton(
                link='plugins:netbox_inventory:audittrailsource_bulk_import',
                title='Импорт',
                icon_class='mdi mdi-upload',
                permissions=['netbox_inventory.add_audittrailsource'],
            ),
        ],
    ),
)

#
# Menu
#

if get_plugin_config('netbox_inventory', 'top_level_menu'):
    # главное меню верхнего уровня
    menu = PluginMenu(
        label='Складской учёт',
        groups=(
            ('Управление активами', assets_items),
            ('Поставки', deliveries_items),
            ('Аудит', audit_admin_items),
        ),
        icon_class='mdi mdi-clipboard-text-multiple-outline',
    )
else:
    # отображение внутри общего раздела плагинов
    menu_items = assets_items + deliveries_items + audit_admin_items
