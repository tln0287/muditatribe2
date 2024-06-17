// Datepicker
$(function () {
    $('#datePicker').datepicker({
        dateFormat: "dd-M-yy",
        changeYear: "true",
        changeMonth: "true",
        yearRange: '-90:+0',
        // minDate: new Date(new Date().setDate(new Date().getDate() - 30)),
        //startDate: "07/16/1989",
        minDate: new Date()
    });
});


// Autocomplete
$(function () {
    var availableTags = [
        "ActionScript",
        "AppleScript",
        "Asp",
        "BASIC",
        "C",
        "C++",
        "Clojure",
        "COBOL",
        "ColdFusion",
        "Erlang",
        "Fortran",
        "Groovy",
        "Haskell",
        "Java",
        "JavaScript",
        "Lisp",
        "Perl",
        "PHP",
        "Python",
        "Ruby",
        "Scala",
        "Scheme"
    ];
    $("#autoComplete").autocomplete({
        source: availableTags
    });
});



//Daterange pikcer
var nowDate = new Date();
today = nowDate.getDate() + '/' + nowDate.getMonth() + '/' + nowDate.getFullYear();
$('#dateRangePicker').daterangepicker({
    //endDate:today,
    autoUpdateInput: false,
    showDropdowns: true,
    locale: {
        cancelLabel: 'Clear'
    },
    ranges: {
        'Today': [moment(), moment()],
        'Yesterday': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
        'Last 7 Days': [moment().subtract(6, 'days'), moment()],
        'Last 30 Days': [moment().subtract(29, 'days'), moment()],
        'This Month': [moment().startOf('month'), moment().endOf('month')],
        'Last Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
    },
    linkedCalendars: false,
    maxDate: moment().endOf("day")
}, function (start, end, label) {
    $('#demo').val('Calendar');
    if (label == 'Today' || label == 'Yesterday') {
        $('#dateRangePicker').val(start.format('DD-MMM-YYYY'));
    }
    else {
        $('#dateRangePicker').val(start.format('DD-MMM-YYYY') + ' to ' + end.format('DD-MMM-YYYY'));
    }
});



// Datatables
$('#dataTable').DataTable({
    // "pageLength": 5
});

// Datatable file exports
$("#dataTableFile").DataTable({
    "pageLength": 10,
    "dom": 'Blfrtip',
    // "language": {
    //     "lengthMenu": "Entries _MENU_ "
    // },
    responsive: true,
    buttons: [
        {
            extend: 'pdf',
            text: 'PDF',
            orientation: 'portrait', // or Landscape
            title: 'File name',
            pageSize: 'A4'
        },
        {
            extend: 'excel',
            text: 'Excel',
            title: 'File name',

        },
        {
            extend: 'csv',
            text: 'CSV',
            title: 'FIle name',

        },
        {
            extend: 'copy',
            text: 'Copy',
            title: 'File name',
        }
    ]

});

// Datatable Column Filter Widgets
$("#columnFilterDatatable").DataTable({
    "pageLength": 10,
    dom: 'W<"clear">Blfrtip',

    // "oColumnFilterWidgets": {
    //     "aiExclude": [0]
    // },
    responsive: true,
    buttons: [
        {
            extend: 'pdf',
            text: 'PDF',
            orientation: 'portrait', // or Landscape
            title: 'File name',
            pageSize: 'A4'
        },
        {
            extend: 'excel',
            text: 'Excel',
            title: 'File name',

        },
        {
            extend: 'csv',
            text: 'CSV',
            title: 'FIle name',

        },
        {
            extend: 'copy',
            text: 'Copy',
            title: 'File name',
        }
    ]

});


// Modal popup
function myModal() {
    $("#myModal").modal('show');
}


//Ckeditor
CKEDITOR.replace('editor', {

});

// Sweet alerts
// Alert Modal Type
$(document).on('click', '#success', function (e) {
    swal({
        title: "Success",
        text: "You clicked the Success button!",
        type: "success",
        icon: "success",
        closeOnClickOutside: false,
        allowOutsideClick: false
    })
});

$(document).on('click', '#error', function (e) {

    swal({
        title: "Error!",
        text: "You clicked the error button!",
        type: "error",
        icon: "error",
        closeOnClickOutside: false,
        allowOutsideClick: false
    })


});

$(document).on('click', '#warning', function (e) {
    swal({
        title: "Warning!",
        text: "You clicked the warning button!",
        type: "warning",
        icon: "warning",
        closeOnClickOutside: false,
        allowOutsideClick: false
    })


});

$(document).on('click', '#info', function (e) {
    swal({
        title: "Info!",
        text: "You clicked the Info button!",
        type: "info",
        icon: "info",
        closeOnClickOutside: false,
        allowOutsideClick: false
    })


});

$(document).on('click', '#question', function (e) {
    swal({
        title: "Question!",
        text: "You clicked the Question button!",
        type: "question",
        icon: "question",
        closeOnClickOutside: false,
        allowOutsideClick: false
    })

});




// Alert With Input Type
$(document).on('click', '#subscribe', function (e) {
    swal({
        title: 'Submit email to subscribe',
        input: 'email',
        inputPlaceholder: 'Example@email.xxx',
        showCancelButton: true,
        confirmButtonText: 'Submit',
        showLoaderOnConfirm: true,
        closeOnClickOutside: false,
        allowOutsideClick: false,
        preConfirm: (email) => {
            return new Promise((resolve) => {
                setTimeout(() => {
                    if (email === 'example@email.com') {
                        swal.showValidationError(
                            'This email is already taken.'
                        )
                    }
                    resolve()
                }, 2000)
            })
        },
        allowOutsideClick: false
    }).then((result) => {
        if (result.value) {
            swal({
                type: 'success',
                title: 'Thank you for subscribe!',
                html: 'Submitted email: ' + result.value
            })
        }
    })
});

// Alert Redirect to Another Link
$(document).on('click', '#link', function (e) {
    swal({
        title: "Are you sure?",
        text: "You will be redirected to URL",
        type: "warning",
        confirmButtonText: "Yes, visit link!",
        showCancelButton: true,
        closeOnClickOutside: false,
        allowOutsideClick: false,
    })
        .then((result) => {
            if (result.value) {
                // window.location = 'https://utopian.io';
            } else if (result.dismiss === 'cancel') {
                swal(
                    'Cancelled',
                    'Your stay here :)',
                    'error'
                )
            }
        })
});


// Bootstrap steps form

$(document).ready(function () {
    $("#basic-pills-wizard").bootstrapWizard({ tabClass: "nav nav-pills nav-justified" }),
        $("#progrss-wizard").bootstrapWizard({
            onTabShow: function (a, r, i) {
                var t = ((i + 1) / r.find("li").length) * 100;
                $("#progrss-wizard")
                    .find(".progress-bar")
                    .css({ width: t + "%" });
            },
        });
});
var triggerTabList = [].slice.call(document.querySelectorAll(".twitter-bs-wizard-nav .nav-link"));
triggerTabList.forEach(function (a) {
    var r = new bootstrap.Tab(a);
    a.addEventListener("click", function (a) {
        a.preventDefault(), r.show();
    });
});


// Select2
$("#multiSelect1").select2({
    // maximumSelectionLength: 2
    placeholder: "Select skill",
    allowClear: true,
    closeOnSelect: false,
    // minimumResultsForSearch: 20
});
$("#multiSelect2").select2({
    // maximumSelectionLength: 2
    placeholder: "Select skill",
    allowClear: true,
    closeOnSelect: false,
    // minimumResultsForSearch: 20
});
$("#multiSelect3").select2({
    // maximumSelectionLength: 2
    placeholder: "Select skill",
    allowClear: true,
    closeOnSelect: false,
    // minimumResultsForSearch: 20
});



// Datetimepicker

window.datetimepicker = new tempusDominus.TempusDominus(
    document.getElementById("datetimepicker"),
    {
        localization: {
            format: 'dd-MMM-yyyy hh:mm T',
        },
        display: {
            icons: {
                time: 'bi bi-clock',
                date: 'bi bi-calendar',
                up: 'bi bi-arrow-up',
                down: 'bi bi-arrow-down',
                previous: 'bi bi-chevron-left',
                next: 'bi bi-chevron-right',
                today: 'bi bi-calendar-check',
                clear: 'bi bi-trash',
                close: 'bi bi-x',
            },
            buttons: {
                today: true,
                clear: true,
                close: true
            }
        }
    }
);

// Time picker

window.timepicker = new tempusDominus.TempusDominus(
    document.getElementById("timepicker"),
    {
        localization: {
            format: 'hh:mm T',
        },
        display: {
            viewMode: "clock",
            components: {
                decades: false,
                year: false,
                month: false,
                date: false,
                hours: true,
                minutes: true,
                seconds: false
            }
        }
    }
);



