$( document ).ready(function() {
    const $recipeGrid = $('#recipe-flex-container');
    const $recipeItems = $('.recipe-item');

    $('.link-icon').on('click', function (e) {
        window.open($(this).data('recipelink'));
    });

    $('#add-recipe').on('click', function (e) {
        $('#modal-container').toggle();
    });

    $('#modal-container').on('click', function (e) {
        if (e.target === $(this).get(0)) {
            $(this).toggle();
        }
    });

    $recipeItems.on('click', function(e) {
        $(this).toggleClass('expanded');
        $(this).find('.img-overlay').toggleClass('light-img-overlay');
        $(this).find('.toolbar').toggleClass('show');
    });

    function setupFlexes() {
        let cols = Math.floor(window.innerWidth / 350);
        let recipeItems = $recipeItems;
        let itemsInCol = Math.ceil(recipeItems.length / cols);

        let startIndex = 0;
        let slices = [];
        while (startIndex < recipeItems.length) {
            if (startIndex + itemsInCol > recipeItems.length) {
                slices.push(recipeItems.slice(startIndex, recipeItems.length));
            } else {
                slices.push(recipeItems.slice(startIndex, startIndex + itemsInCol));
            }
            startIndex += itemsInCol;
        }
        for (let i = 0; i < cols; i++) {
            let $flex = $('<div/>', {
                'class': 'vertical-flex',
            });
            $recipeGrid.append($flex);

            for (let j = 0; j < slices[i].length; j++) {
                $flex.append(slices[i][j])
            }
        }
    }

    window.onload = function () {
      setupFlexes();
      $('#loading').fadeOut();
      $recipeGrid.css('display', 'flex');
    };

    window.onresize = function () {
        if ($recipeGrid.children().length !== Math.floor(window.innerWidth / 350)) {
            setupFlexes();
        }
    };
});
