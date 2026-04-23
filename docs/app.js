// ============================================================
// ACLAS Neuro-Edu v3 — Full Frontend Logic
// Three.js 3D Nebula (inside nebula panel) + Chart.js + D3.js Knowledge Graph
// ============================================================

// ── 3D Three.js Nebula (scoped to #agent-3d-container) ──────
let scene, camera, renderer, particleSystem, agentSpheres = [];
let threeInitialized = false;

function init3D() {
    const host = document.getElementById('agent-3d-container');
    if (!host || threeInitialized) return;
    threeInitialized = true;

    const w = host.clientWidth || 700;
    const h = host.clientHeight || 400;

    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(60, w / h, 0.1, 3000);
    camera.position.set(0, 0, 450);

    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(w, h);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.domElement.style.cssText = 'position:absolute;top:0;left:0;width:100%;height:100%;border-radius:20px';
    host.appendChild(renderer.domElement);

    // Background star field (latent space representation)
    const N = 1200;
    const geo = new THREE.BufferGeometry();
    const pos = new Float32Array(N * 3);
    const col = new Float32Array(N * 3);
    for (let i = 0; i < N; i++) {
        pos[i*3]   = (Math.random() - 0.5) * 900;
        pos[i*3+1] = (Math.random() - 0.5) * 900;
        pos[i*3+2] = (Math.random() - 0.5) * 700;
        // Subtle cyan/purple mix
        const t = Math.random();
        col[i*3]   = t * 0.6;
        col[i*3+1] = 0.7 + t * 0.3;
        col[i*3+2] = 1.0;
    }
    geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    geo.setAttribute('color', new THREE.BufferAttribute(col, 3));
    particleSystem = new THREE.Points(geo, new THREE.PointsMaterial({
        size: 2.0, vertexColors: true, transparent: true, opacity: 0.5,
        blending: THREE.AdditiveBlending, depthWrite: false
    }));
    scene.add(particleSystem);

    // Resize observer to handle panel resize
    new ResizeObserver(() => {
        const w2 = host.clientWidth;
        const h2 = host.clientHeight;
        if (w2 && h2) {
            camera.aspect = w2 / h2;
            camera.updateProjectionMatrix();
            renderer.setSize(w2, h2);
        }
    }).observe(host);

    animate3D();
}

let animFrame;
function animate3D() {
    animFrame = requestAnimationFrame(animate3D);
    if (!particleSystem) return;
    particleSystem.rotation.y += 0.0005;
    particleSystem.rotation.x += 0.00015;
    const t = Date.now() * 0.001;
    agentSpheres.forEach((s, i) => {
        const r = 90 + i * 12;
        const speed = 0.3 + i * 0.02;
        s.position.x = Math.cos(t * speed + i * 0.52) * r;
        s.position.y = Math.sin(t * speed * 0.7 + i * 0.8) * (r * 0.6);
        s.position.z = Math.sin(t * 0.4 + i * 0.3) * 80;
        s.rotation.y += 0.02;
    });
    renderer.render(scene, camera);
}

function updateAgentSpheres(agents) {
    if (!scene) return;
    agentSpheres.forEach(s => { scene.remove(s); s.geometry.dispose(); s.material.dispose(); });
    agentSpheres = [];
    agents.forEach((a, i) => {
        const r = 8 + a.attention * 10;
        const geo = new THREE.SphereGeometry(r, 10, 10);
        const mat = new THREE.MeshBasicMaterial({
            color: new THREE.Color(moodToHex(a.mood)),
            transparent: true, opacity: 0.25 + a.attention * 0.45,
            wireframe: true
        });
        const sphere = new THREE.Mesh(geo, mat);
        scene.add(sphere);
        agentSpheres.push(sphere);
    });
}

function flashNebula(rgb = [0, 0.9, 1.0]) {
    if (!particleSystem) return;
    const col = particleSystem.geometry.attributes.color.array;
    for (let i = 0; i < col.length; i += 3) {
        col[i] = rgb[0]; col[i+1] = rgb[1]; col[i+2] = rgb[2];
    }
    particleSystem.geometry.attributes.color.needsUpdate = true;
    setTimeout(() => {
        for (let i = 0; i < col.length; i += 3) {
            const t = Math.random();
            col[i] = t * 0.6; col[i+1] = 0.7 + t * 0.3; col[i+2] = 1.0;
        }
        particleSystem.geometry.attributes.color.needsUpdate = true;
    }, 1000);
}

// ── Chart.js ─────────────────────────────────────────────────
let lossChart, moodChart, skillChart;
Chart.defaults.color = '#666';
Chart.defaults.borderColor = 'rgba(255,255,255,0.05)';

function initCharts() {
    lossChart = new Chart(document.getElementById('chart-loss'), {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'MSE Loss (Federated Avg)',
                data: [],
                borderColor: '#00f2ff',
                backgroundColor: 'rgba(0,242,255,0.06)',
                borderWidth: 2, pointRadius: 2.5, fill: true, tension: 0.4,
            }]
        },
        options: {
            responsive: true, maintainAspectRatio: false, animation: { duration: 400 },
            scales: {
                x: { title: { display: true, text: 'Training Step', color: '#555' }, ticks: { maxTicksLimit: 12, color: '#555' } },
                y: { title: { display: true, text: 'MSE Loss', color: '#555' }, beginAtZero: true, ticks: { color: '#555' } }
            },
            plugins: { legend: { labels: { color: '#888' } } }
        }
    });

    moodChart = new Chart(document.getElementById('chart-mood'), {
        type: 'doughnut',
        data: {
            labels: ['Excited', 'Focused', 'Confused', 'Neutral'],
            datasets: [{ data: [0,0,0,0], backgroundColor: ['#00f2ff','#00ff88','#ff3366','#444'], borderWidth: 0, hoverOffset: 8 }]
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            plugins: { legend: { labels: { color: '#888', padding: 16 } } }
        }
    });

    skillChart = new Chart(document.getElementById('chart-skill'), {
        type: 'radar',
        data: {
            labels: ['Logic', 'Math', 'Language', 'Memory', 'Creative'],
            datasets: [{
                label: 'Class Avg Skills',
                data: [0,0,0,0,0],
                borderColor: '#9d00ff', backgroundColor: 'rgba(157,0,255,0.12)',
                pointBackgroundColor: '#9d00ff', pointRadius: 4, borderWidth: 2,
            }]
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            scales: { r: { min: 0, max: 1, ticks: { stepSize: 0.25, color: '#555', backdropColor: 'transparent' }, grid: { color: 'rgba(255,255,255,0.06)' }, pointLabels: { color: '#888', font: { size: 12 } } } },
            plugins: { legend: { labels: { color: '#888' } } }
        }
    });
}

// ── D3.js Knowledge Graph ────────────────────────────────────
function renderKnowledgeGraph(graphData) {
    const svg = d3.select('#kg-svg');
    svg.selectAll('*').remove();
    const w = document.getElementById('kg-svg').clientWidth;
    const h = document.getElementById('kg-svg').clientHeight;

    if (!graphData.nodes.length) {
        svg.append('text').attr('x', w/2).attr('y', h/2).attr('text-anchor', 'middle')
           .attr('fill', '#444').attr('font-size', 13).text('No concepts indexed yet — run a broadcast first.');
        return;
    }

    const sim = d3.forceSimulation(graphData.nodes)
        .force('link', d3.forceLink(graphData.edges).id(d => d.id).distance(120))
        .force('charge', d3.forceManyBody().strength(-250))
        .force('center', d3.forceCenter(w/2, h/2))
        .force('collision', d3.forceCollide(28));

    const defs = svg.append('defs');
    defs.append('marker').attr('id', 'arr').attr('viewBox', '0 -4 10 8')
        .attr('refX', 22).attr('markerWidth', 6).attr('markerHeight', 6).attr('orient', 'auto')
        .append('path').attr('d', 'M0,-4L10,0L0,4').attr('fill', 'rgba(0,242,255,0.35)');

    const link = svg.append('g').selectAll('line').data(graphData.edges).enter()
        .append('line').attr('stroke', 'rgba(0,242,255,0.18)').attr('stroke-width', d => 1 + d.weight * 2)
        .attr('marker-end', 'url(#arr)');

    const nodeG = svg.append('g').selectAll('g').data(graphData.nodes).enter().append('g')
        .call(d3.drag()
            .on('start', (e, d) => { if (!e.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; })
            .on('drag', (e, d) => { d.fx = e.x; d.fy = e.y; })
            .on('end', (e, d) => { if (!e.active) sim.alphaTarget(0); d.fx = null; d.fy = null; }));

    nodeG.append('circle')
        .attr('r', d => 12 + (d.count || 1) * 4)
        .attr('fill', 'rgba(0,242,255,0.06)').attr('stroke', 'rgba(0,242,255,0.5)').attr('stroke-width', 1.5);

    nodeG.append('text').attr('dy', 4).attr('text-anchor', 'middle')
        .attr('fill', 'rgba(200,230,255,0.7)').style('font-size', '9px').style('pointer-events', 'none')
        .text(d => d.label.slice(0, 14));

    sim.on('tick', () => {
        link.attr('x1', d => d.source.x).attr('y1', d => d.source.y)
            .attr('x2', d => d.target.x).attr('y2', d => d.target.y);
        nodeG.attr('transform', d => `translate(${d.x},${d.y})`);
    });
}

// ── Tabs ─────────────────────────────────────────────────────
let currentTab = 'nebula';
function switchTab(tab) {
    currentTab = tab;
    ['nebula','loss','graph','mood'].forEach(t => {
        document.getElementById(`view-${t}`).style.display = t === tab ? '' : 'none';
    });
    document.querySelectorAll('.tab-btn').forEach(b => {
        b.classList.toggle('active', b.dataset.tab === tab);
    });
    if (tab === 'nebula') {
        // Reinit 3D if not yet done (first tab switch might need it)
        setTimeout(init3D, 50);
    }
    if (tab === 'graph') fetchAndRenderGraph();
}

// ── Helpers ───────────────────────────────────────────────────
function moodToHex(mood) {
    return { Excited: '#00f2ff', Focused: '#00ff88', Confused: '#ff3366' }[mood] || '#555555';
}

// ── API ───────────────────────────────────────────────────────
async function api(path, opts = {}) {
    const r = await fetch(path, opts);
    return r.json();
}

async function fetchAndRenderGraph() {
    const data = await api('/api/graph');
    renderKnowledgeGraph(data);
}

// ── Main UI Update ────────────────────────────────────────────
async function updateUI() {
    let status, metrics;
    try {
        [status, metrics] = await Promise.all([api('/api/status'), api('/api/metrics')]);
    } catch (e) { console.warn('API offline', e); return; }

    // Header stats
    document.getElementById('h-tick').textContent = String(status.tick).padStart(4, '0');
    document.getElementById('h-gpa').textContent  = metrics.gpa != null ? metrics.gpa.toFixed(2) : '—';
    document.getElementById('h-cas').textContent  = metrics.cas != null ? metrics.cas.toFixed(4) : '—';
    document.getElementById('h-ret').textContent  = metrics.retention_rate != null ? `${(metrics.retention_rate * 100).toFixed(0)}%` : '—';

    // 3D nebula agents
    updateAgentSpheres(status.agents);

    // Charts
    if (metrics.loss_curve?.length) {
        lossChart.data.labels = metrics.loss_curve.map((_, i) => i + 1);
        lossChart.data.datasets[0].data = metrics.loss_curve;
        lossChart.update('none');
    }
    if (metrics.mood_distribution) {
        const md = metrics.mood_distribution;
        moodChart.data.datasets[0].data = [md.Excited||0, md.Focused||0, md.Confused||0, md.Neutral||0];
        moodChart.update('none');
    }
    if (metrics.skill_distribution) {
        const sd = metrics.skill_distribution;
        skillChart.data.datasets[0].data = [sd.logic||0, sd.math||0, sd.language||0, sd.memory||0, sd.creative||0];
        skillChart.update('none');
    }

    // Right panel
    renderAgentList(status.agents);
    renderDropoutRisk(metrics.dropout_risk || []);
    document.getElementById('rp-count').textContent = `AGENTS: ${status.agents.length}`;
}

function renderAgentList(agents) {
    const el = document.getElementById('agent-list');
    el.innerHTML = '';
    agents.forEach(a => {
        const card = document.createElement('div');
        card.className = 'agent-card';
        card.style.borderLeftColor = moodToHex(a.mood);
        const skillsHtml = Object.entries(a.skills).map(([k, v]) => `
            <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px">
                <span style="width:64px;font-size:11px;color:#8090a8;text-transform:uppercase;letter-spacing:0.04em;font-weight:500">${k}</span>
                <div style="flex:1;height:4px;background:rgba(255,255,255,0.08);border-radius:3px;overflow:hidden">
                    <div style="height:100%;width:${v*100}%;background:${moodToHex(a.mood)};border-radius:3px;transition:width 0.8s;opacity:0.85"></div>
                </div>
                <span style="width:30px;font-size:11px;color:#9aacbe;text-align:right;font-family:'JetBrains Mono'">${(v*100).toFixed(0)}</span>
            </div>`).join('');
        card.innerHTML = `
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
                <span style="font-weight:700;font-size:15px;color:#e8f0f8">${a.name}</span>
                <span style="font-size:11px;padding:3px 12px;border-radius:20px;background:rgba(255,255,255,0.06);color:${moodToHex(a.mood)};font-weight:600">${a.mood}</span>
            </div>
            <p style="font-size:11px;color:#8090a0;font-style:italic;margin-bottom:10px;line-height:1.5">"${a.thought}"</p>
            ${skillsHtml}
            <div style="display:flex;justify-content:space-between;margin-top:8px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);font-size:11px;font-family:'JetBrains Mono';color:#6a7a90">
                <span>ATTN <span style="color:#aabcc8">${(a.attention*100).toFixed(0)}%</span></span>
                <span>PROB <span style="color:#aabcc8">${a.prob.toFixed(3)}</span></span>
                <span>KN <span style="color:#aabcc8">${a.knowledge_count}</span></span>
            </div>`;
        el.appendChild(card);
    });
}

function renderDropoutRisk(risks) {
    const sec = document.getElementById('risk-section');
    const lst = document.getElementById('risk-list');
    if (!risks.length) { sec.style.display = 'none'; return; }
    sec.style.display = '';
    lst.innerHTML = risks.slice(0, 5).map(r => `
        <div style="display:flex;justify-content:space-between;align-items:center;padding:6px 12px;background:rgba(255,51,102,0.06);border-radius:8px;margin-bottom:5px">
            <span style="font-size:12px;color:#ddd">${r.name}</span>
            <span style="font-size:11px;color:#ff3366;font-family:'JetBrains Mono'">Risk ${r.risk.toFixed(3)}</span>
        </div>`).join('');
}

// ── Controls ──────────────────────────────────────────────────
document.getElementById('rng-complex').oninput = function() {
    document.getElementById('lbl-complex').textContent = parseFloat(this.value).toFixed(2);
};

document.getElementById('btn-teach').onclick = async function() {
    const text = document.getElementById('txt-instruction').value.trim() || 'Axiomatic instruction stream initiated.';
    const complexity = parseFloat(document.getElementById('rng-complex').value);
    const domain = document.getElementById('sel-domain').value;
    this.disabled = true; this.textContent = 'Syncing...';
    try {
        await api('/api/teach', {
            method: 'POST', headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ text, complexity, skills_req: { [domain]: 0.8 } })
        });
        flashNebula([0, 0.9, 1.0]);
        await updateUI();
    } finally {
        this.disabled = false; this.textContent = 'Initiate Broadcast';
    }
};

document.getElementById('btn-train').onclick = async function() {
    this.disabled = true; this.textContent = 'Training...';
    const box = document.getElementById('train-result');
    box.style.display = '';
    box.innerHTML = '<span style="color:#666">Running federated backpropagation...</span>';
    try {
        const data = await api('/api/train', { method: 'POST' });
        flashNebula([0.6, 0, 1.0]);
        if (data.error) {
            box.innerHTML = `<span style="color:#ff3366">ERROR: ${data.error}</span>`;
        } else {
            box.innerHTML = `<span style="color:#00ff88">✓ Training complete — ${data.samples_per_agent} samples/agent</span><br><br>` +
                data.epoch_losses.map((l, i) => `<span style="color:#666">Epoch ${i+1}:</span> <span style="color:#00f2ff">${l.toFixed(6)}</span>`).join('<br>');
        }
        await updateUI();
    } finally {
        this.disabled = false; this.textContent = 'Run Federated Training';
    }
};

document.getElementById('btn-reset').onclick = async function() {
    if (!confirm('Reset all agent states and training history?')) return;
    await api('/api/reset', { method: 'POST' });
    document.getElementById('train-result').style.display = 'none';
    flashNebula([0.5, 0.5, 0.5]);
    await updateUI();
};

// ── Architecture ──────────────────────────────────────────────
async function loadArchInfo() {
    try {
        const d = await api('/api/architecture');
        document.getElementById('arch-info').innerHTML =
            `[${d.architecture?.join(' → ')}]<br>${d.total_params} params · ${d.optimizer} · ${d.loss_fn}`;
    } catch {}
}

// ── Boot ──────────────────────────────────────────────────────
// Wire up tab buttons
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.onclick = () => switchTab(btn.dataset.tab);
});

// Init sequence
initCharts();
loadArchInfo();
updateUI().then(() => {
    // Delay 3D init slightly to ensure container is laid out
    setTimeout(init3D, 100);
});

setInterval(updateUI, 7000);
