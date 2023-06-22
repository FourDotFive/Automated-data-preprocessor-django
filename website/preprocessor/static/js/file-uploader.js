document.addEventListener("DOMContentLoaded", () => {
    var uploadButton = document.getElementById('uploadButton');
    var fileInput = document.getElementById('id_file');

    uploadButton.addEventListener('click', function () {
        fileInput.click();
    });
});

document.addEventListener("DOMContentLoaded", () => {
    var fileInput = document.getElementById('id_file');

    fileInput.addEventListener('change', function () {
        if (this.files && this.files.length > 0) {
            // Check the number of files
            if (this.files.length > 1) {
                Swal.fire({
                    title: 'Error!',
                    text: 'You can only upload one file',
                    icon: 'error',
                    confirmButtonColor: '#6DA9E4',
                });
                this.value = '';
                return;
            }

            // Check the file type
            var file = this.files[0];
            if (file.type !== 'text/csv' && file.type !== 'text/plain') {
                Swal.fire({
                    title: 'Error!',
                    text: 'The file must be a .csv or .txt file',
                    icon: 'error',
                    confirmButtonColor: '#6DA9E4',
                });
                this.value = '';
                return;
            }

            var extension = file.name.split('.').pop().toLowerCase();
            console.log(extension);
            if (extension !== 'csv' && extension != 'txt') {
                Swal.fire({
                    title: 'Error!',
                    text: 'The file must be a .csv or .txt file',
                    icon: 'error',
                    confirmButtonColor: '#6DA9E4',
                });
                this.value = '';
                return;
            }
        }

        submitFile();

    });

});


function dropHandler(ev) {
    console.log('File(s) dropped');
    ev.preventDefault();

    document.getElementById('dropOverlay').style.display = 'none';

    var files = ev.dataTransfer.files;

    // Check the number of files
    if (files.length > 1) {
        Swal.fire({
            title: 'Error!',
            text: 'You can only upload one file',
            icon: 'error',
            confirmButtonColor: '#6DA9E4',
        });
        return;
    }

    // Check the file type
    var file = files[0];
    if (file.type !== 'text/csv' && file.type !== 'text/plain') {
        Swal.fire({
            title: 'Error!',
            text: 'The file must be a .csv or .txt file',
            icon: 'error',
            confirmButtonColor: '#6DA9E4',
        });
        return;
    }

    console.log(file.name);

    document.getElementById('id_file').files = files;

    submitFile();
}

function dragOverHandler(ev) {
    ev.preventDefault();
    document.getElementById('dropOverlay').style.display = 'block';
}

function dragLeaveHandler(ev) {
    if (ev.currentTarget.contains(ev.relatedTarget)) {
        return;
    }
    ev.preventDefault();
    document.getElementById('dropOverlay').style.display = 'none';
}

function submitFile() {
    var fileInput = document.getElementById('id_file');
    Swal.fire({
        title: 'Please provide the delimiter for your CSV or TXT file:',
        html: `<input id="delimiter-input" class="form-control no-outline" type="text" value=";" style="width: 70px; display: inline-block; outline: none" />
                <button id="delimiter-submit" class="btn no-outline" style="display: inline-block">Submit</button>`,
        showConfirmButton: false,
        didOpen: () => {
            const input = Swal.getPopup().querySelector('#delimiter-input')
            const button = Swal.getPopup().querySelector('#delimiter-submit')
            button.onclick = () => {
                console.log(input.value);
                if (!input.value) {
                    Swal.showValidationMessage('You need to write something!')
                } else {
                    // Perform your actions here with input.value as the delimiter
                    document.getElementById('id_delimiter').value = input.value;

                    document.getElementById('submit-button').click();
                    Swal.close()
                }
            }
        },
        willClose: () => {
            fileInput.value = '';
        }
    })
}