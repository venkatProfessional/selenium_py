import os
from selenium.webdriver.support.select import Select
from selenium_helper.common_code import CommonCode
from DataDrivenTesting import XLutility
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


class GettingReportFromExcel:
    def __init__(self):
        self.helper = CommonCode()
        self.driver = self.helper.driver
        self.helper.open_url("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
        self.helper.wait()

        file = os.path.join("C:\\Users", "JothiVenkatajalapath", "Desktop", "Working_with_py", "Book1.xlsx")

        try:
            rows = XLutility.getRowCount(file, "Sheet4")
        except Exception as e:
            print(f"Error reading Excel: {e}")
            return

        for r in range(2, rows + 1):
            principal = XLutility.readData(file, "Sheet4", r, 1)
            rate = XLutility.readData(file, "Sheet4", r, 2)
            period1 = XLutility.readData(file, "Sheet4", r, 3)
            period2 = XLutility.readData(file, "Sheet4", r, 4)
            frequency_val = XLutility.readData(file, "Sheet4", r, 5)
            expected_maturity = XLutility.readData(file, "Sheet4", r, 6)

            # Check for missing data
            if None in [principal, rate, period1, period2, frequency_val, expected_maturity]:
                print(f"\n❗ Row {r} has missing data. Skipping.")
                XLutility.writeData(file, "Sheet4", r, 8, "Skipped - Missing Data")
                XLutility.fillRedColor(file, "Sheet4", r, 8)
                continue

            print(f"\nRow {r} → {principal}, {rate}, {period1}, {period2}, {frequency_val}, Expected: {expected_maturity}")

            # Input values
            self.driver.find_element(By.ID, "principal").clear()
            self.driver.find_element(By.ID, "principal").send_keys(str(principal))

            self.driver.find_element(By.ID, "interest").clear()
            self.driver.find_element(By.ID, "interest").send_keys(str(rate))

            self.driver.find_element(By.ID, "tenure").clear()
            self.driver.find_element(By.ID, "tenure").send_keys(str(period1))

            # Select Period2 dropdown
            select_year = Select(self.driver.find_element(By.ID, "tenurePeriod"))
            available_options = [option.text.strip() for option in select_year.options]
            cleaned_period2 = str(period2).strip()

            if cleaned_period2 not in available_options:
                print(f"Invalid period2 value '{cleaned_period2}' not in dropdown. Skipping row {r}")
                XLutility.writeData(file, "Sheet4", r, 8, "Skipped - Invalid Period")
                XLutility.fillRedColor(file, "Sheet4", r, 8)
                continue
            select_year.select_by_visible_text(cleaned_period2)

            # Select frequency
            frequency_dropdown = Select(self.driver.find_element(By.ID, "frequency"))
            frequency_options = [opt.text.strip() for opt in frequency_dropdown.options]
            cleaned_freq = str(frequency_val).strip()

            if cleaned_freq not in frequency_options:
                print(f"Invalid frequency value '{cleaned_freq}' not in dropdown. Skipping row {r}")
                XLutility.writeData(file, "Sheet4", r, 8, "Skipped - Invalid Frequency")
                XLutility.fillRedColor(file, "Sheet4", r, 8)
                continue
            frequency_dropdown.select_by_visible_text(cleaned_freq)

            # Close overlay if present
            try:
                overlay = self.driver.find_element(By.CLASS_NAME, "wzrk-overlay")
                close_button = self.driver.find_element(By.CLASS_NAME, "wzrk-close")
                close_button.click()
                self.helper.wait(1)
                print("Closed overlay popup.")
            except NoSuchElementException:
                pass

            # Try clicking calculate button
            try:
                calculate_btn = self.driver.find_element(By.XPATH, "//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']")
                calculate_btn.click()
            except ElementClickInterceptedException:
                print("Click intercepted. Retrying with JavaScript...")
                self.driver.execute_script("document.querySelector('.wzrk-overlay')?.remove();")
                self.driver.execute_script("document.querySelector('.wzrk-modal')?.remove();")
                calculate_btn.click()

            self.helper.wait()

            actual_result = self.driver.find_element(By.ID, "resp_matval").text.replace(",", "").strip()
            print(f"Expected: {expected_maturity}, Actual: {actual_result}")

            try:
                if float(expected_maturity) == float(actual_result):
                    print("✅ Test Passed")
                    XLutility.writeData(file, "Sheet4", r, 8, "Passed")
                    XLutility.fillGreenColor(file, "Sheet4", r, 8)
                else:
                    print("❌ Test Failed")
                    XLutility.writeData(file, "Sheet4", r, 8, "Failed")
                    XLutility.fillRedColor(file, "Sheet4", r, 8)
            except ValueError as ve:
                print(f"Value error comparing expected vs actual: {ve}")
                XLutility.writeData(file, "Sheet4", r, 8, "Error")
                XLutility.fillRedColor(file, "Sheet4", r, 8)

            # Clear the form
            clear_btn = self.driver.find_element(By.XPATH, "//img[@class='PL5']")
            clear_btn.click()
            self.helper.wait(1)


if __name__ == "__main__":
    GettingReportFromExcel()