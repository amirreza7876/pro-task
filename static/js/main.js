document.getElementById('invalid_login').style.color='red';
// document.getElementById('id_username')[0].placeholder='username'
document.forms['reg_form']['username'].placeholder='username';
var form = document.forms['login'];

function remove_offer(){
  var offer = document.getElementById('offer');
  offer.parentNode.removeChild(offer);
  return false;
}
