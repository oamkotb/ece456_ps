(function () {
	window.SENSUS_CFG = {
		ltiDomain: 'https://inside.sensusaccess.com/',

		clientId: '262750000000000038',
		consumerKey: '0d63f184-5521-4185-c117-08ddadaf75b4'
	}

	$('<script>').attr('src', SENSUS_CFG.ltiDomain + 'js/canvasui/sensus-main.js').appendTo('body')
})()