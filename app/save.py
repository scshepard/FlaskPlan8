
@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    form = LoginForm()
    """
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    """
    """
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    """
    flash("Getting ready to do Sign In")
    #user = User.query.filter_by(email=resp.email).first()
    remember_me = True
    nickname = "scs"
    email = "scs@scs.com"
    user = User(nickname=nickname, email=email)
    db.session.add(user)
    db.session.commit()
    # make the user follow him;herself
    db.session.add(user.follow(user))
    db.session.commit()
    user.id = 1

    if user is None:
        user = User(nickname=nickname, email=email)
        db.session.add(user)
        db.session.commit()
        flash("making user %s",nickname)

    login_user(user, remember=remember_me)
    return render_template('index.html',
                           title='Home',
                           user=user)

