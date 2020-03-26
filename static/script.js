function register_change() {
    const login_form = document.querySelector('form.login-form');
    const log_button = document.querySelector('button.log-button');
    const reg_label = document.querySelector('p.reg-label');
    const bad_login = document.querySelector('p.bad-login');
    const reg_link = document.createElement('a');
    if (bad_login != null){
        bad_login.remove()
    }
    login_form.setAttribute('action', '/register_user');

    log_button.innerText = 'Register';
    reg_label.innerText = 'Already have an account? ';

    reg_link.innerText = 'Login';
    reg_link.setAttribute('class','reg-link')
    reg_link.setAttribute('onclick','login_change()')
    reg_label.appendChild(reg_link)
}


function login_change() {
    const login_form = document.querySelector('form.login-form');
    const log_button = document.querySelector('button.log-button');
    const reg_label = document.querySelector('p.reg-label');
    const reg_link = document.createElement('a');

    login_form.setAttribute('action', '/login_user');

    log_button.innerText = 'Login';
    reg_label.innerText = 'Don`t have an account yet? ';

    reg_link.innerText = 'Register';
    reg_link.setAttribute('class','reg-link')
    reg_link.setAttribute('onclick','register_change()')
    reg_label.appendChild(reg_link)
}