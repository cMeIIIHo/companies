$(document).ready(function () {

  BX24.init(function(){

    Vue.component('company_id', {
      props: ['id'],
      template: `<li>ID: {{ id }}</li>`
    });

    Vue.component('each_name_block', {
      props: ['name'],
      template: `
        <li>Для компании с названием "{{ name.name }}" зарегистрированы дубликаты с идентификаторами:
          <ul>
            <company_id
              v-for="id in name.ids"
              v-bind:id="id"
              v-bind:key="id">
            </company_id>
          </ul>
        </li>
      `
    });

    var vm = new Vue({
      el: '#vm',
      data: {
        duplicates: []
      },
      methods: {
        show_duplicates: function() {
          this.duplicates = []
          var self = this;
          $.ajax({
            url: 'http://127.0.0.1:8000/api/get_duplicates',
            type: 'POST',
            data: BX24.getAuth(),
            dataType: 'json',
            success: function(duplicates){
              for(var index in duplicates) {
                self.duplicates.push(duplicates[index])
              }
            }
          })
        }
      }
    });
  });
});

