(function($) {
    $(document).ready(function() {
        var province_select = $('#id_province');
        var city_select = $('#id_city');

        function filterCities() {
            var province_id = province_select.val();

            if (province_id) {
                var url = '/customer/get-cities/?province=' + province_id;

                $.ajax({
                    url: url,
                    success: function(response) {
                        var city_options = '<option value="">---------</option>';
                        response.forEach(function(city) {
                            city_options += '<option value="' + city.id + '">' + city.name + '</option>';
                        });
                        city_select.html(city_options);
                    }
                });
            } else {
                city_select.html('<option value="">---------</option>');
            }
        }

        province_select.change(function() {
            filterCities();
        });

        if (!province_select.val()) {
            city_select.html('<option value="">---------</option>');
        } else {
            filterCities();
        }
    });
})(django.jQuery);