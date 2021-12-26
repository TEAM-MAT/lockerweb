<h1>API명세</h1>
<ol>
  <li><h2>예약</h2></li>
  url은 locker/reserve <br>
  method : POST <br>
  요구사항: request body에 json으로  'lockernum' : 사물함번호(예 : H01001) 형식으로 전송.<br>
  처리 결과는 json으로 코드 200에 result로 사물함 번호가 오면 성공<br>
  코드 403에 result로 'reserved locker'가 오면 이미 예약된것(실패)<br>
  <li><h2>취소</h2></li>
  url은 locker/cancel<br>
  요구사항: post method로 별다른 데이터 없이 request만 보내면 됨<br>
  처리 결과는 200이면 성공, 404면 예약된 사물함이 없어 취소 불가<br>
</ol>