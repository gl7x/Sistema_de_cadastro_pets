document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.querySelector(".caixa-busca input[name='q']");
    const prioritySelect = document.querySelector(".caixa-busca select[name='priority']");
    const taskCards = document.querySelectorAll(".cartao-tarefa");

    const filterCards = () => {
        const query = searchInput?.value.toLowerCase().trim() ?? "";
        const priority = prioritySelect?.value ?? "";

        taskCards.forEach((card) => {
            const title = card.querySelector("h3")?.textContent.toLowerCase() ?? "";
            const badge = card.querySelector(".distintivo")?.textContent ?? "";
            const matchesQuery = query === "" || title.includes(query);
            const matchesPriority = priority === "" || badge === priority;

            card.style.display = matchesQuery && matchesPriority ? "flex" : "none";
        });
    };

    searchInput?.addEventListener("input", filterCards);
    prioritySelect?.addEventListener("change", filterCards);
});