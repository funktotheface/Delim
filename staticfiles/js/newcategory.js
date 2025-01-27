
document.addEventListener('DOMContentLoaded', function() {
    const categorySelect = document.getElementById('id_category');
    const newCategoryInput = document.getElementById('div_id_new_category');
    

    function toggleNewCategoryInput() {
        if (categorySelect.value) {               
            newCategoryInput.value = '';
            newCategoryInput.style.display = 'none';
        } else {
            newCategoryInput.style.display = 'block';
        }
    }

    categorySelect.addEventListener('change', toggleNewCategoryInput);
    toggleNewCategoryInput();
});
