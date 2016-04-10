$(document).ready(function(){
$("#btn_confirm").click(function(){
		var username = $("#user_name").val();
		var email = $("#user_email").val();
		var password = $("#user_pwd").val();
		var password_repeat = $("#user_pwd_repeat").val();
		if(username.length ==0){
			alert("请填写用户名");
			return ;
		}
		if(email.length == 0){
			alert("请填写邮箱");
			return ;
		}
		if(password.length == 0){
			alert("请填写密码");
			return ;
		}
		if (password != password_repeat && password.length >10){
			alert("两次密码不一样!");
			return;
		}
		if (username.length<8 || username.length >30) {
			alert("用户名不合法");
			return;
		}
		$.getJSON("/sprout/reg",{name:username,email:email,pwd:password},function(ret){
			if (ret.success){
				alert("register success");
			} else {
				alert("register failed\nreason:"+ret.reason);
			}
		});
	});
});