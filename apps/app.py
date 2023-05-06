from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/paddingandmargin')
def paddingandmargin():
	return render_template('paddingAndMargin.html')

@app.route('/floatanddisplay')
def floatanddisplay():
	return render_template('floatanddisplay.html')

@app.route('/position')
def position():
	return render_template('position.html')

@app.route('/opacityborderradius')
def opacityborderradius():
	return render_template('opacityborderradius.html')

@app.route('/style')
def sytle():
	return render_template('style.html')

@app.route('/flex')
def flex():
	return render_template('flex.html')

@app.route('/animation')
def anumation():
	return render_template('animation.html')

@app.route('/test01')
def test01():
	return render_template('test01.html')

@app.route('/zindex')
def zindex():
	return render_template('zindex.html')

@app.route('/test02')
def test02():
	return render_template('test02.html')


@app.route('/test03')
def test03():
	return render_template('test03.html')

@app.route('/test04')
def test04():
	return render_template('test04.html')

@app.route('/test05')
def test05():
	return render_template('test05.html')

@app.route('/test06')
def test06():
	return render_template('test06.html')
