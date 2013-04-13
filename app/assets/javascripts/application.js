(function(namespace) {

  // Models
  var User = can.Model({},{});

  // Controls
  var Login = can.Control({
    init: function() {
      this.element.html(can.view('/static/views/login.ejs'));
    },

    onConnected: function() {
      var self = this;
      console.log('logged in');
      FB.api('/me', function(response) {
        //self.options.user = User.model(response);
        new Home('#home', {user: response});
        $('#app').attr('page', 'home');
      });
    },
    
    '.login click': function(el, event) {
      var self = this;
      FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
          self.onConnected();
        } else {
          FB.login(function() {self.onConnected()});
        }
      });
    },
  });

  var Home = can.Control({
    init: function() {
      console.log(this.options);
      this.element.html(can.view('/static/views/home.ejs', this.options));
    }
  });


  // Start
  $(function() {
    namespace.login = new Login('#login');
  });

  namespace.Login = Login;
  namespace.Home = Home;

})(window);
