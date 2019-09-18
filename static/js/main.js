document.getElementById('invalid_login').style.color='red';
var form = document.forms['login'];

function remove_offer(){
  var offer = document.getElementById('offer');
  offer.parentNode.removeChild(offer);
  return false;
}
