$(document).ready(function () {
    let isLoadingData = false;

    $('.scrollable').on('scroll', function () {
        if (!isLoadingData && $(this).scrollTop() + $(this).innerHeight() >= $(this)[0].scrollHeight) {

            if (num_rows > start) {
                isLoadingData = true;
                $.get('/more_data/', { start: start, folder_name: folder_name }, function (data) {
                    console.log(data);
                    start += length;

                    for (var id in data) {
                        var newRow = '<tr>';
                        newRow += '<th>' + id + '</th>';

                        for (var key in data[id]) {
                            newRow += '<td>' + data[id][key] + '</td>';
                        }

                        newRow += '</tr>';
                        $('#data-table').append(newRow);
                    }
                    isLoadingData = false;
                });
            }

        }
    });

});