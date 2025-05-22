<?php 

    $dados = [
        "valores" => [406, -2.3122265423263, 1.95199201064158, -1.60985073229769, 3.9979055875468, -5.22187864667764, -1.42654531920595, -2.53738730624579,
                               1.39165724829804, -2.77008927719433, -2.77227214465915, 3.20203320709635, -2.89990738849473, -5.95221881324605, -4.28925378244217,
                               3.89724120274487, -1.14074717980657, -2.83005567450437, -1.68224681808257, 4.16955705037907, 1.26910559061474, 5.17232370861764,
                               -3.50493686052974, -4.65211076182388, 3.20198198514526, 4.45191674731724, 1.77839798284401, 2.61145002567677, -1.43275874698919,
                               0]
    ];

    $options = [
        'http' => [
            'header' => "Content-Type: application/json",
            'method' => "POST",
            'content' => json_encode($dados),
        ]
    ];

    $context = stream_context_create($options);
    $result = file_get_contents('http://localhost:5000/prever', false, $context);
    $response = json_decode($result, true);

    if($response['fraude']){
        echo '<h1 style="text-align: center;">⚠️ Transação suspeita de fraude!</h1>';
    } else {
        echo '<h1 style="text-align: center;">✅ Transação segura.</h1>';
    }