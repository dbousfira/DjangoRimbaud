/* Project specific Javascript goes here. */
const user_input = $("#user-input")
const articles_div = $('#replaceable-content')
const endpoint = '/articles/'
const delay_by_in_ms = 350
let scheduled_function = false

let ajax_call = function (endpoint, request_parameters) {
    $.getJSON(endpoint, request_parameters)
    .done(response => {
        // fade out the articles_div, then:
            articles_div.fadeTo('slow', 0).promise().then(() => {
                // replace the HTML contents
                articles_div.html(response['html_from_view'])
                // fade-in the div with new contents
                articles_div.fadeTo('slow', 1)
            })
        })
}


user_input.on('keyup', function () {

    const request_parameters = {
        q: $(this).val() // value of user_input: the HTML element with ID user-input
    }

    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})