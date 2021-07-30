"use strict";


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
	branch_pre = "1GOB";
	break;
    case '3':
	branch_pre = "3POL";
	break;
    case '4':
	branch_pre = "4CBE";
	break;
    case '5':
	branch_pre = "5TPR";
	break;
    case '6':
	branch_pre = "6ERD";
	break;
    case '7':
	branch_pre = "7DGL";
	break;
    case '8':
	branch_pre = "8KRR";
	break;
    default:
	branch_pre = "2MLR";
  }
  document.getElementById("branch").value = branch_pre;
});
