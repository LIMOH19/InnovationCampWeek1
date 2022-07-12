

function done_bucket(continent) {
            $.ajax({
                type: "GET",
                url: "/reviews/continent",
                data: {continent_give: continent},
                success: function (response) {
                }
            });
        }