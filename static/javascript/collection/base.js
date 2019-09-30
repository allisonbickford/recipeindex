$( document ).ready(function() {
    const $recipeGrid = $('#recipe-flex-container');
    const baseWidth = $recipeGrid.children().eq(0).width();

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


    $('.recipe-item').on('click', function(e) {
        let recipeDetails = $('#recipe-'+ $(this).data('recipepk'));
        let currentHeight = $recipeGrid.height();

        // let newHeight = currentHeight + $(this).find('.recipe-title').height() + recipeDetails.get(0).scrollHeight;
        // $recipeGrid.height(newHeight.toString() + 'px');

        $(this).toggleClass('expanded');
        $(this).find('.recipe-title').toggleClass('full');
        if (!$(this).hasClass('expanded')) {
            // setFlexHeight();
        }
    });

    function setFlexHeight() {
        let cols = Math.floor(window.innerWidth / baseWidth);
        let itemsInCol = Math.ceil($recipeGrid.children().length / cols);
        let maxItemHeight = 250;
        for (let i = 0; i < $recipeGrid.children().length; i++) {
            const currentHeight = $recipeGrid.children().eq(i).height();
            if (currentHeight > maxItemHeight) {
                maxItemHeight = currentHeight;
            }
        }
        $recipeGrid.height(itemsInCol * maxItemHeight);
    }

    function setupFlexes() {
        let cols = Math.floor(window.innerWidth / 350);
        let recipeItems = $('.recipe-item');
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
        console.log(slices.length)
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
