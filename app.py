from flask import Flask, render_template

app = Flask(__name__)

# Configure Flask
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable caching during development


@app.route('/')
def index():
    """Landing page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')


@app.route('/portfolio')
def portfolio():
    """Portfolio page"""
    return render_template('portfolio.html')


@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 page"""
    return render_template('index.html'), 404


if __name__ == '__main__':
    # Run the app in debug mode for development
    # Set debug=False for production
    app.run(debug=True, host='0.0.0.0', port=5001)
