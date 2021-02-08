function check(){
  var input_univ = document.getElementById( "id_da-xue-ming" ).value ;
  var univ_etc = document.getElementById( "id_sonota-woxuan-ze-saretachang-he-ha-kochiraworu-li-shitekudasai" ).value ;
  var input_data = document.getElementById( "id_yan-jiu-ke" ).value ;
  var yourself = document.getElementById( "id_u3053u81eau8eabu306bu3064u3044u3066" ).value ;
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
        if (yourself == "未選択"){
          alert("ご自身についてお答えください！");
          return false;
        }
          else{
          return true;
        }
      }
    }
  }
  else{
    if (input_data == "研究科"){
      alert("研究科名を入力してください!");
      return false;
    }
    else{
      if (yourself == "未選択"){
        alert("ご自身についてお答えください！");
        return false;
      }
        else{
        return true;
      }
    }
  }
}
