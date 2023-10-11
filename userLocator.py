class elem:
    username = "username"
    password = "password"
    loginButton = "orangehrm-login-button"
    menuAdmin = "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']/span[.='Admin']"
    userManagementDropdown = "//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[1]/span[@class='oxd-topbar-body-nav-tab-item']"
    usersOption = "//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li"
    editButton = "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[1]/div[@role='row']/div[6]/div/button[2]/i"
    usernameEdit = "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[4]/div/div[2]/input"
    userRole = "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]/div/div[2]/div[@class='oxd-select-wrapper']/div//i"
    userRoleChoose = "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']//div[@role='listbox']/div[3]/span[.='ESS']"
    saveButton = "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']"
    # notifSuccess = "//div[@id='oxd-toaster_1']/div//p[@class='oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']"
    notifSuccess = "//div[@id='oxd-toaster_1']/div//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']"
    # notifSuccess = "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']"
    checkboxChangePassword = "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[5]//i"
    passwordChange = "//div[@id='app']//form[@class='oxd-form']/div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div//input[@type='password']"
    confirmPassChange = "//div[@id='app']//form[@class='oxd-form']/div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@type='password']"
    errorMessageUsername = "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']//span[.='Should be at least 5 characters']"
    errorMessagePasswordNotMatch = "//div[@id='app']//form[@class='oxd-form']/div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div/span[.='Passwords do not match']"
    errorMessagePassShouldHave7Char = "//div[@id='app']//form[@class='oxd-form']/div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div/span[.='Should have at least 7 characters']"
    trashIcon = "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[3]/div[@role='row']/div[6]/div/button[1]/i"
    confirmDelete = "//div[@id='app']/div[@role='dialog']//div[@role='document']/div[@class='orangehrm-modal-footer']/button[2]"
    notifSuccessDelete = "//div[@id='oxd-toaster_1']/div//p[@class='oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']"
    deleteSelectedButton = "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='button']"
