//■依存関係
//TreeObject,JQuery

class Sticky{
	static cnt = 0;
	static list = 0;
	static active_sticky_id      = "";
	static active_sticky_url     = "";
	static active_sticky_title   = "";
	static active_sticky_content = "";
	static active_sticky_status  = 0;
	static active_sticky_top     = 5;
	static active_sticky_left    = 5;
	static active_sticky_height  = 10;
	static active_sticky_width   = 10;
	static active_sticky_color   = "#ffffff";
	
	constructor(url){
		this.xhr = new XMLHttpRequest();
		this.set_xhr();
		this.send_button = null;
		this.response_sticky_id = "";
	}
	
	set_xhr(){
		let self = this;
		this.xhr.onload = function(){
			let READYSTATE_COMPLETED = 4;
			let HTTP_STATUS_OK = 200;
			if( this.readyState == READYSTATE_COMPLETED && this.status == HTTP_STATUS_OK ){
				let sticky_id = self.response_sticky_id;
				if(sticky_id != ""){
					document.getElementById("sticky_status_" + sticky_id).innerHTML = this.responseText;
				}
			}
		}
		return this;
	}
	
	//■POST送信する関数
	send(){
		let data = {
			"title"     : Sticky.active_sticky_title
			,"content"  : Sticky.active_sticky_content
			,"status"   : Sticky.active_sticky_status
			,"top"      : Sticky.active_sticky_top   
			,"left"     : Sticky.active_sticky_left  
			,"height"   : Sticky.active_sticky_height
			,"width"    : Sticky.active_sticky_width 
			,"color"    : Sticky.active_sticky_color 
		};
		this.response_sticky_id = Sticky.active_sticky_id;
		console.log(Sticky.active_sticky_url,data);
		this.xhr.open("POST",Sticky.active_sticky_url);
		this.xhr.setRequestHeader( 'Content-Type', 'application/json' );
		this.xhr.send(JSON.stringify(data));
	}
	
	
}

