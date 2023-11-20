function showDiary(url) {
    var date = url.split('/').pop();
    alert('Clicked date: ' + date);
    
    // ここで必要に応じてAjaxを使用してサーバーサイドに日付を送信するなどの処理を追加できます。
}
