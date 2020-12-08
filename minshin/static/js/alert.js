function check(){
  /*フォームに応じてアラートの有無を切り分ける*/
  var input_data = document.getElementById("id_rate").value ;

  if (input_data == 0){
    alert("フォームを入力してください！")
  }
}
