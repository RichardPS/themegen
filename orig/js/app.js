// jscs:disable
$(function() {

    var App = {

        start: function() {

            // Twitter configuration options
            $('#tweets').tweet({
                join_text: 'auto',
                username: 'PrimarySiteLtd',
                avatar_size: 32,
                auto_join_text_default: 'PrimarySiteLtd said',
                loading_text: 'Checking for new tweets...',
                count: 1
            });

            ps.scrollingBanner('.scrolling-banner');

        }
    };

    // Run the functions in the start object
    App.start();

});
