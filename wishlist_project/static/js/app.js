document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/items/')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('kanban');
            if (data.length) {
                let html = '<ul>';
                data.forEach(item => {
                    const checkbox = item.status ? "[x]" : "[ ]";
                    html += `<li>${checkbox} ${item.name} - R$ ${item.price}</li>`;
                });
                html += '</ul>';
                container.innerHTML = html;
            } else {
                container.innerHTML = '<p>Nenhum item encontrado.</p>';
            }
        })
        .catch(error => {
            console.error('Erro ao buscar os itens:', error);
        });
});