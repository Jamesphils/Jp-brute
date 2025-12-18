import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from playwright.sync_api import sync_playwright
import password_manager

class AutoFillApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AutoFill Login")
        
        # URL entry
        tk.Label(self.root, text="Enter full login URL:").grid(row=0, column=0)
        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.grid(row=0, column=1)
        
        # Email selector
        tk.Label(self.root, text="Email field selector:").grid(row=1, column=0)
        self.email_entry = tk.Entry(self.root, width=50)
        self.email_entry.grid(row=1, column=1)
        
        # Password selector
        tk.Label(self.root, text="Password field selector:").grid(row=2, column=0)
        self.password_entry = tk.Entry(self.root, width=50)
        self.password_entry.grid(row=2, column=1)
        
        # Submit button selector
        tk.Label(self.root, text="Submit button selector:").grid(row=3, column=0)
        self.submit_entry = tk.Entry(self.root, width=50)
        self.submit_entry.grid(row=3, column=1)
        
        # Start button
        tk.Button(self.root, text="Start", command=self.start).grid(row=4, column=1)
        
        # Result log
        self.result_text = ScrolledText(self.root, width=70, height=15)
        self.result_text.grid(row=5, column=0, columnspan=2, pady=10)

    def log(self, message):
        self.result_text.insert(tk.END, message + "\n")
        self.result_text.see(tk.END)
        self.result_text.update()

    def start(self):
        site_url = self.url_entry.get()
        email_selector = self.email_entry.get()
        password_selector = self.password_entry.get()
        submit_selector = self.submit_entry.get()
        credentials = password_manager.passwords

        if not credentials:
            self.log("No valid credentials found in password_manager.py")
            return

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            try:
                page = browser.new_page()
                page.goto(site_url)
                for cred in credentials:
                    try:
                        self.log(f"Trying {cred['email']}...")
                        page.fill(email_selector, cred['email'])
                        page.fill(password_selector, cred['password'])
                        page.click(submit_selector)
                        # Wait a short time for page update
                        page.wait_for_timeout(2000)
                        # Check if logout or dashboard element exists
                        if page.locator('text=Logout').count() > 0:
                            self.log(f"Success: {cred['email']} + {cred['password']}")
                            return
                        else:
                            self.log("Login failed, trying next credential...")
                    except Exception as e:
                        self.log(f"Error with {cred['email']}: {str(e)}")
            finally:
                browser.close()
        self.log("No working credentials found.")

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = AutoFillApp()
    app.run()