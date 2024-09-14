# AssignmentXAPI
Disclaimer: *AssignmentX is no longer in development*
AssignmentXAPI is wraper api for android app to generate handwritten assignemnts. For web based version click [here](https://github.com/dedsec995/AssignmentX)

## Installation
### Prerequisites
- Python 3.6 or higher
- Flask
- Pillow
- Requests
- Werkzeug
- Debudding skills

### Setiing Up
1. Clone the repo:
```bash
git clone https://github.com/dedsec995/assignmentx.git
cd assignmentx
```
2. Install Dependencies:
```bash
pip install -r requirements.txt
```
3. Configure the Upload Folder:
Ensure the `UPLOAD_FOLDER` path in `app.py` is correctly set to a writable directory on your system.

4. Run the Application:
```bash
python app.py
```

## Usage
### Api Endpoints
- `GET /`
Returns a welcome message
- `POST /api/assignmentx`
Accepts Json data and fiels to generate a handwritten assignment. The expected Json format is:
```json
{
  "name": "Assignment Name",
  "opacity": 255,
  "color1": "#ff0000",
  "color2": "#00ff00",
  "wtext": "Sample text content",
  "opage": "blankPage",
  "sfont": "no"
}
```
- `name`: The name of the assignment.
- `opacity`: Opacity of the text.
- `color1 and color2`: Text colors in hex format.
- `wtext`: Text content to be included in the PDF.
- `opage`: Page template to use.
- `sfont`: Whether to use a custom font or default.
Files can be uploaded as part of the request
