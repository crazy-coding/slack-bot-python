
const state = {
  id: null,
  name: null
};

const getters = {
  id() {
    return state.id;
  },
  name() {
    return state.name;
  }
};

const actions = {
  load(context, payload) {
    context.commit('load', payload);
    return payload;
  },
  unload(context, payload) {
    context.commit('unload', payload);
    return payload;
  }
};

const mutations = {
  load(state, user) {
    state.id = user.id;
    state.name = user.name;
    state.errors = {};
  },
  unload(state) {
    state.id = null;
    state.name = null;
    state.errors = {};
  }
};

export default {
  namespaced: true,
  state: state,
  actions: actions,
  mutations: mutations,
  getters: getters
};