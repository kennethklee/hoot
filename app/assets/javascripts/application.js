(function(namespace) {

  // Models

  // Controls
  var Login = can.Control({
    init: function() {
      console.log(this);
      this.element.html(can.view('/static/views/login.ejs'));
    },
    
    '#loginToFacebook click': function(el, event) {
      FB.login();
    }
  });


  // Start
  $(function() {
    namespace.login = new Login('#login');
    
  });

  namespace.Login = Login;

})(window);
