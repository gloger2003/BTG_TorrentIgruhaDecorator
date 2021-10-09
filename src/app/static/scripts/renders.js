function render_gp_content(url) {
    $.ajax({
        url: '/render_gp_content' + url,
        type: 'get',
        success: function(response) {
            $('#content-block').remove();
            $('#pagination-block').remove();
            $('#main').append(response)

            let cards = $('.game-preview-card').toArray();
            cards.forEach(element => {
                $.ajax({
                    url: '/get_game_preview_desc/' + element.getAttribute("href"),
                    type: 'get',
                    success: function(response) {
                        $(element).find('.preview-data').find('.desc').html(response);
                    }
                })
            });
        },
        error: function() {
            $('#content-block').html('<h1>Не получилось найти игры :(</h1>')
        }
    });
}

function render_genres_content() {
    $.ajax({
        url: '/render_genres_content',
        type: 'get',
        success: function(response) {
            $('#content-block').remove();
            $('#main').append(response)
        },
        error: function() {
            $('#content-block').html('<h1>Не получилось найти категории игр :(</h1>')
        }
    });
}