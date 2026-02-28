document.addEventListener('DOMContentLoaded', function () {
    const input = document.getElementById('nationality-input');
    if (!input) return;

    const dropdown = document.createElement('ul');
    dropdown.style.cssText = 'position:absolute;background:#fff;border:1px solid #ccc;list-style:none;padding:0;margin:0;z-index:1000;min-width:200px;';
    input.parentNode.style.position = 'relative';
    input.parentNode.appendChild(dropdown);

    input.addEventListener('input', async function () {
        const q = this.value;
        if (q.length < 1) { dropdown.innerHTML = ''; return; }

        const res = await fetch(`/api/v1/actors/autocomplete/nationality/?q=${q}`);
        const data = await res.json();

        dropdown.innerHTML = '';
        data.results.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item;
            li.style.cssText = 'padding:6px 12px;cursor:pointer;';
            li.addEventListener('mouseenter', () => li.style.background = '#f0f0f0');
            li.addEventListener('mouseleave', () => li.style.background = '#fff');
            li.addEventListener('click', () => {
                input.value = item;
                dropdown.innerHTML = '';
            });
            dropdown.appendChild(li);
        });
    });

    document.addEventListener('click', e => {
        if (!input.parentNode.contains(e.target)) dropdown.innerHTML = '';
    });
});