"use strict";

/*
document.getElementById("branch").disabled = true;
document.getElementById("loan_no").addEventListener("blur", function(){
  const loan_number = document.getElementById("loan_no").value;
  let branch_code;
  const char = String(loan_number[2]);

  const numbers = ['1', '2', '3', '4', '5', '6', '7', '8'];

  if (numbers.includes(char)) {
    branch_code = loan_number[2];
  } else {
      branch_code = loan_number[3];
  }

  let branch_pre;
  switch(branch_code) {

    case '1':
	branch_pre = "0";
	break;
    case '3':
	branch_pre = "2";
	break;
    case '4':
	branch_pre = "3";
	break;
    case '5':
	branch_pre = "4";
	break;
    case '6':
	branch_pre = "5";
	break;
    case '7':
	branch_pre = "6";
	break;
    case '8':
	branch_pre = "7";
	break;
    default:
	branch_pre = "1";
  }
  const select_branch = document.getElementById("branch");
  select_branch.selectedIndex = branch_pre;
  console.log(select_branch.textContent);
});
*/

document.addEventListener("DOMContentLoaded", function() {
  const today = new Date();
  const d = String(today.getDate()).padStart(2, '0');
  const m = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
  const y = today.getFullYear();
  const today_date = y + '-' + m + '-'+ d;
  console.log(today_date)
  document.getElementById("today").value = today_date;
});
