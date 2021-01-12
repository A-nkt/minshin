/*
フォーム入力値の適正化を行う
１　大学名が「その他」の場合、記入があるか？
２　研究科名は「研究科」だけではなく入力がなされているか？
*/
function check(){
  var input_univ = document.getElementById( "id_da-xue-ming" ).value ;
  var univ_etc = document.getElementById( "id_sonota-woxuan-ze-saretachang-he-ha-kochiraworu-li-shitekudasai" ).value ;
  var input_data = document.getElementById( "id_yan-jiu-ke" ).value ;
  if (input_univ == "その他"){
    if (univ_etc == "" ){
      alert("その他を選択した場合は、大学名を入力してください!");
      return false
    }
    else{
      if (input_data == "研究科"){
        alert("研究科名を入力してください!");
        return false;
      }
      else{
        return true;
      }
    }
  }
  else{
    if (input_data == "研究科"){
      alert("研究科名を入力してください!");
      return false;
    }
    else{
      return true;
    }
  }
}
