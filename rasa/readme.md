# Setting up the Virtual Environment

1. **Create a Virtual Environment:**
   ```bash
   python3 -m venv myenv   ```

2. **Activate the Virtual Environment:**

   - **On Windows:**     ```bash
     myenv\Scripts\activate     ```

   - **On macOS and Linux:**     ```bash
     source myenv/bin/activate     ```

3. **Install Packages and Update `requirements.txt`:**
   ```bash
   pip install <package_name>
   pip freeze > requirements.txt   ```

   Replace `<package_name>` with the actual package you want to install.

4. **Deactivate the Virtual Environment:**

   To deactivate the virtual environment, simply run:
   ```bash
   deactivate   ```
