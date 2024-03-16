const environment = {
  "PORT": "8000",
  "HOST": "localhost"
}
const interpreterPath = "C:\\Users\\samar\\OneDrive\\Desktop\\Development\\myProjects\\FastOCR\\venv\\Scripts\\pythonw.exe"

module.exports = {
        apps: [
          {
            name: "Start Fast-OCR",
            script: 'main.py',
            interpreter: interpreterPath,
            args: [],
            autorestart: true,
            log_date_format: 'YYYY-MM-DD HH:mm:ss',
            error_file: 'NULL',
            out_file: 'NULL',
            max_restarts: 10,
            exec_mode: 'fork',
            exec_args: ['-u'],
            env: {...environment}
          },
        ],
      };
      