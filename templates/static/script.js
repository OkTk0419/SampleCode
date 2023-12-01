function showDiary(url) {
    var date = url.split('/').pop();
    alert('日付: ' + date + '日');
    // alert("日付: " + day + "\n年: " + year + "\n月: " + month);
    // ここで必要に応じてAjaxを使用してサーバーサイドに日付を送信するなどの処理を追加できます。
}
