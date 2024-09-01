(function($) {
    $(document).ready(function() {
        var province_select = $('#id_province');
        var city_select = $('#id_city');

        function filterCities() {
            var province_id = province_select.val();

            if (province_id) {
                var url = window.location.pathname + '?province=' + province_id;

                $.ajax({
                    url: url,
                    success: function(response) {
                        var city_options = $(response).find('#id_city').html();
                        city_select.html(city_options);
                    }
                });
            } else {
                city_select.html('<option value="">---------</option>');
            }
        }

        province_select.change(function() {
            filterCities();  // Refresh the city field when the province is changed
        });

        // Initially empty city select if no province is selected
        if (!province_select.val()) {
            city_select.html('<option value="">---------</option>');
        } else {
            filterCities();  // Populate cities if a province is already selected
        }
    });
})(django.jQuery);