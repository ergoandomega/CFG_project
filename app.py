from flask import Flask, request, flash, make_response, render_template, redirect
from quotes import get_motivational_quote
from profile import calculate_bmi, get_fitness_goal
from recipes import Recipes
from fitness import Fitness
from user_management import add_user, check_email_not_in_use, check_login_details, \
    get_user_info, update_weight, update_height, \
    requires_sign_in, requires_sign_out

app = Flask(__name__)
app.secret_key = 'abcd'


@app.get('/')
def home():
    return redirect('/signin')


@app.get('/signin')
@requires_sign_out
def signin():
    return render_template('signin.html', quote=get_motivational_quote())


@app.post('/signin')
def submit_signin():
    email = request.form.get('email')
    password = request.form.get('password')
    user_id = check_login_details(email, password)
    if not user_id:
        flash('Could not sign in. Incorrect details')
        return redirect('/signin')
    response = make_response(redirect('/profile'))
    response.set_cookie('user_id', str(user_id))
    return response


@app.post('/signout')
@requires_sign_in
def submit_signout():
    response = make_response(redirect('/signin'))
    response.delete_cookie('user_id')
    return response


@app.get('/signup')
@requires_sign_out
def signup():
    return render_template('signup.html', quote=get_motivational_quote())


@app.post('/signup')
def submit_signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    email_not_in_use = check_email_not_in_use(email)
    if email_not_in_use:
        add_user(name, email, password)
        flash('Sign up successful')
        return redirect('/signin')
    else:
        flash('There is already an account with that email address')
        return redirect('/signup')


@app.get('/profile')
@requires_sign_in
def profile():
    user_id = request.cookies.get('user_id')
    user_info = get_user_info(user_id)
    if user_info['height'] and user_info['weight']:
        user_info['bmi'] = calculate_bmi(user_info['height'], user_info['weight'])
        user_info['goal'] = get_fitness_goal(user_info['bmi'])
    return render_template('profile.html', user_info=user_info, quote=get_motivational_quote())


@app.post('/profile')
@requires_sign_in
def submit_profile_info():
    user_id = request.cookies.get('user_id')
    height = request.form.get('height')
    if height:
        update_height(height, user_id)
    weight = request.form.get('weight')
    if weight:
        update_weight(weight, user_id)
    return redirect('/profile')


@app.get('/recipes')
@requires_sign_in
def recipes():
    ingredient = request.args.get('ingredient')
    if ingredient:
        recipes_for_ingredient = Recipes.get_recipes_for_ingredient(ingredient)
    else:
        recipes_for_ingredient = None
    return render_template('recipes.html', recipes=recipes_for_ingredient, quote=get_motivational_quote())


@app.get('/fitness')
@requires_sign_in
def fitness():
    random_exercises = Fitness.get_random_exercises()
    return render_template('fitness.html', exercises=random_exercises, quote=get_motivational_quote())


app.run(debug=True)
